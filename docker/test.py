import influxdb_client, os, time, base64, requests, shutil, random, boto3, uuid, datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from botocore.client import Config
from requests.auth import HTTPDigestAuth

###ADD hosts to etc
with open('/etc/hosts', 'a') as f:
    f.write('192.168.243.10    minio.localdev.me\n')
    f.write('192.168.243.10    influxdb.localdev.me\n')
 


### Get file
current_time = datetime.datetime.now()
time_stamp = current_time.timestamp()
#date_time = datetime.datetime.fromtimestamp(time_stamp)

path=f"/tmp/{time_stamp}.jpg"
urlcam='http://192.168.100.189/ISAPI/Streaming/channels/1/picture?snapShotImageType=JPEG'
passcam = 'q12345678'
usercam = 'admin'
rescam = requests.get(urlcam, auth=HTTPDigestAuth(str(usercam), str(passcam)), stream = True)
if rescam.status_code == 200:
    with open(path,'wb') as f:
        shutil.copyfileobj(rescam.raw, f)



#TO influx

token = "EbPGslDdSFMtUsTKWXUBOfabTG1xPkJwo1nTyn558u7mqluzzuLQ93ZMX2_MIrERM-oedY738kQa2VJRIwzAog=="
org = "primary"
url = "http://influxdb.localdev.me"
bucket="primary"
write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

with open(path, 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')


    print(base64_message)


point = (
  Point("cams")
  # .tag(random.randint(1, 5), "cnt")
  .field("cnt", random.randint(1, 5))
  .field("img", str(base64_message))
)
write_api.write(bucket=bucket, org="primary", record=point)