import os, time, base64, requests, shutil, random, socket, datetime
from requests.auth import HTTPDigestAuth
from minio import Minio
from minio.error import S3Error

def getfile(path, urlcam):
    '''
    Получаем картинку с камеры
    '''
    # passcam = os.environ.get('CAM_PASS')
    # usercam = os.environ.get('CAM_USER')
    passcam = 'q12345678'
    usercam = 'admin'
    rescam = requests.get(urlcam, auth=HTTPDigestAuth(str(usercam), str(passcam)), stream = True)
    if rescam.status_code == 200:
        with open(path,'wb') as f:
            shutil.copyfileobj(rescam.raw, f)



print ("Hello!!!")
print("Now =", datetime.datetime.now())
print("Hostname =", socket.gethostname())
print("Home dir =", os.path.expanduser('~'))
getfile('/tmp/file.jpg', 'http://192.168.100.171/Streaming/channels/1/picture?snapShotImageType=JPEG')



def main():
  # Create a client with the MinIO server playground, its access key
  # and secret key.
  client = Minio(
    endpoint='http://minio.localdev.me',
    secure=True,
    access_key='XB99WjybqXeYFmUIZ85b',
    secret_key='dnua23hXltL1MpgWsHzQmg4Se6vFNdzjmLMTKFXs'
  )

  # Make 'asiatrip' bucket if not exist.
  found = client.bucket_exists("test")
  if not found:
    client.make_bucket("test")
  else:
    print("Bucket 'test' already exists")

  # Upload '/home/user/Photos/asiaphotos.zip' as object name
  # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
  client.fput_object(
    "test", "foto", "/tmp/file.jpg",
  )
  print(
    "'/tmp/file.jpg' is successfully uploaded as "
    "object 'file.jpg' to bucket 'test'."
  )


if __name__ == "__main__":
  try:
    main()
  except S3Error as exc:
    print("error occurred.", exc)