import  os, time, base64, requests, shutil, random, boto3, uuid, datetime
from botocore.client import Config
from requests.auth import HTTPDigestAuth


s3 = boto3.resource('s3',
                    endpoint_url='http://minio.localdev.me',
                    aws_access_key_id='XB99WjybqXeYFmUIZ85b',
                    aws_secret_access_key='dnua23hXltL1MpgWsHzQmg4Se6vFNdzjmLMTKFXs',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

# upload a file from local file system '/home/john/piano.mp3' to bucket 'songs' with 'piano.mp3' as the object name.

#s3.Bucket('test').upload_file(str(ptf), str(file), ExtraArgs={'ContentType': 'image/jpeg'})

def download_folder(bucket_name, s3_folder, local_dir=None):
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        bucket.download_file(obj.key, target)

# download the object 'piano.mp3' from the bucket 'songs' and save it to local FS as /tmp/classical.mp3
s3.Bucket('test').download_file('1695185536.642843.jpg', '/tmp/filed.jpg')
download_folder('test', 'dir', '/tmp/dir')

print ("download 'file.jpg' as  finale")


 