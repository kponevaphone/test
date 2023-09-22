import  os, time, base64, requests, shutil, random, boto3, uuid, datetime
from botocore.client import Config
from requests.auth import HTTPDigestAuth

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



s3 = boto3.resource('s3',
                    endpoint_url='http://minio.localdev.me',
                    aws_access_key_id='XB99WjybqXeYFmUIZ85b',
                    aws_secret_access_key='dnua23hXltL1MpgWsHzQmg4Se6vFNdzjmLMTKFXs',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

# upload a file from local file system '/home/john/piano.mp3' to bucket 'songs' with 'piano.mp3' as the object name.
file = os.listdir(path='/tmp')[0]
ptf = f'/tmp/{file}'
s3.Bucket('test').upload_file(str(ptf), str(file), ExtraArgs={'ContentType': 'image/jpeg'})
os.remove(ptf)


# download the object 'piano.mp3' from the bucket 'songs' and save it to local FS as /tmp/classical.mp3
#s3.Bucket('songs').download_file('piano.mp3', '/tmp/classical.mp3')

print ("upload 'file.jpg' as  finale")


 