import  os, time, base64, requests, shutil, random, uuid, datetime, socket
from PIL import Image 
from os import path
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from requests.auth import HTTPDigestAuth
from defisheye import Defisheye
from ultralytics import YOLO
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

###ADD hosts to etc
with open('/etc/hosts', 'a') as f:
    f.write('192.168.243.10    minio.localdev.me\n')
    f.write('192.168.243.10    influxdb.localdev.me\n')
 

def myfun(pth):
    print(pth[:-4])
    print(pth)
    pt0=f"{pth[:-4]}_0.jpg"
    jp1=f"{pth[:-4]}_1.jpg"
    jp2=f"{pth[:-4]}_2.jpg"
    jp3=f"{pth[:-4]}_3.jpg"
    jp4=f"{pth[:-4]}_4.jpg"

    Image.open(pth).convert('RGB').save(pt0)
    Image.open(pt0).crop((215, 565, 535, 885)).save(jp1)
    Image.open(jp1).resize((640, 640)).save(jp1)

    Image.open(pt0).crop((520, 420, 1160, 1060)).save(jp2)

    Image.open(pt0).crop((1160, 420, 1480, 1060)).save(jp3)
    im1 = Image.open('bg.jpg')
    im2 = Image.open(jp3)
    im1.paste(im2, (160, 0))
    im1.save(jp3)

    Image.open(pt0).crop((1480, 590, 1800, 910)).save(jp4)
    Image.open(jp4).resize((640, 640)).save(jp4)

def myfun2(pth):
    model1 = YOLO('/app/best.pt')
    im1 = Image.open(pth)
    results = model1.predict(source=im1, save=True, show_labels=False, show_conf=False)  # save plotted images
    boxes = results[0].boxes.data
    return len(boxes)

def myfun3(pth, le):
    token = "cGG4qR3-NxP_CsR9l9CTlKkBfdKgTP9GkpTDOR0f1ZFF-2k-DwHXU9OYKVA3nh3zpwgINE94k-DfDHN0Mcmfog=="
    org = "primary"
    url = "http://influxdb.localdev.me"

    with open(pth, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    bucket="primary"
    write_api = write_client.write_api(write_options=SYNCHRONOUS)


    point = (
    Point("cams")
    # .tag(random.randint(1, 5), "cnt")
    .field("cnt", int(le))
    .field("img", str(base64_message))
    )
    write_api.write(bucket=bucket, org="primary", record=point)
    time.sleep(1) # separate points by 1 second



pt = '/app/picture.jpg'
myfun(pt)
pt = '/app/picture_1.jpg'
my = myfun2(pt)
pt = '/app/runs/detect/predict/picture_1.jpg'
Image.open(pt).rotate(-90).save(pt)
myfun3(pt, my)