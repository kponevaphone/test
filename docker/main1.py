import  os, time, base64, requests, shutil, random, boto3, uuid, datetime
from botocore.client import Config
from requests.auth import HTTPDigestAuth
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from PIL import Image 
from os import path
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from requests.auth import HTTPDigestAuth
from defisheye import Defisheye
from ultralytics import YOLO



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