import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


with open('/etc/hosts', 'a') as f:
    f.write('192.168.243.10    minio.localdev.me\n')
    f.write('192.168.243.10    influxdb.localdev.me\n')
 


token = "EbPGslDdSFMtUsTKWXUBOfabTG1xPkJwo1nTyn558u7mqluzzuLQ93ZMX2_MIrERM-oedY738kQa2VJRIwzAog=="
org = "primary"
url = "http://influxdb.localdev.me"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="primary"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
  point = (
    Point("measurement")
    .tag("tagname", "tagvalue1")
    .field("field", value)
  )
  write_api.write(bucket=bucket, org="primary", record=point)
  time.sleep(1) # separate points by 1 second
