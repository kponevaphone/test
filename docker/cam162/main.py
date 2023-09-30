import  os, time, base64, requests, shutil, random, uuid, datetime, socket, influxdb_client
from PIL import Image 
from os import path
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from requests.auth import HTTPDigestAuth
from defisheye import Defisheye
from ultralytics import YOLO


###ADD hosts to etc
with open('/etc/hosts', 'a') as f:
    f.write('192.168.243.10    minio.localdev.me\n')
    f.write('192.168.243.10    influxdb.localdev.me\n')
 

def getfile(pth):
    ### Get file
    current_time = datetime.datetime.now()
    time_stamp = current_time.timestamp()
    #date_time = datetime.datetime.fromtimestamp(time_stamp)

    urlcam='http://192.168.100.170/ISAPI/Streaming/channels/1/picture?snapShotImageType=JPEG'
    passcam = 'q12345678'
    usercam = 'admin'
    rescam = requests.get(urlcam, auth=HTTPDigestAuth(str(usercam), str(passcam)), stream = True)
    if rescam.status_code == 200:
        with open(pth,'wb') as f:
            shutil.copyfileobj(rescam.raw, f)

def cropimg(pth):
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

def aipredict():
    chph = {}
    path = os.getcwd()
    # чтение записей
    with os.scandir(path) as listOfEntries:  
        for entry in listOfEntries:
            # печать всех записей, являющихся файлами
            if entry.is_file():
                if entry.name.endswith('_1.jpg'):
                    model1 = YOLO('/app/1.pt')
                    im1 = Image.open(entry.name)
                    results1 = model1.predict(source=im1, save=True, show_labels=True, show_conf=True, max_det=4)  # save plotted images
                    boxes1 = len(results1[0].boxes.data)
                    chph.update({0:boxes1})
                    # Image.open('runs/detect/predict/orig_1.jpg').rotate(-90).save('runs/detect/predict/orig_1.jpg')
                    with open('runs/detect/predict/orig_1.jpg', 'rb') as binary_file:
                        binary_file_data = binary_file.read()
                        base64_encoded_data = base64.b64encode(binary_file_data)
                        chph.update({1:base64_encoded_data.decode('utf-8')})

                shutil.rmtree('runs', ignore_errors=True)

                if entry.name.endswith('_2.jpg'):
                    model2 = YOLO('/app/2.pt')
                    im2 = Image.open(entry.name)
                    results2 = model2.predict(source=im2, save=True, show_labels=True, show_conf=True, max_det=4)  # save plotted images
                    boxes2 = len(results2[0].boxes.data)
                    chph.update({2:boxes2})

                    with open('runs/detect/predict/orig_2.jpg', 'rb') as binary_file:
                        binary_file_data = binary_file.read()
                        base64_encoded_data = base64.b64encode(binary_file_data)
                        chph.update({3:base64_encoded_data.decode('utf-8')})

                shutil.rmtree('runs', ignore_errors=True)

                # if entry.name.endswith('_3.jpg'):
                #     model = YOLO('/app/3.pt')
                #     im = Image.open(entry.name)
                #     results = model.predict(source=im, save=True, show_labels=True, show_conf=True, max_det=4)  # save plotted images
                #     boxes = results[0].boxes.data
                #     tati.append(len(boxes))
                # if entry.name.endswith('_4.jpg'):
                    # model = YOLO('/app/4.pt')
                    # im = Image.open(entry.name)
                    # results = model.predict(source=im, save=True, show_labels=True, show_conf=True, max_det=4)  # save plotted images
                    # boxes = results[0].boxes.data
                    # tati.append(len(boxes))
    return chph

def tobase(ptli):
    token = "cGG4qR3-NxP_CsR9l9CTlKkBfdKgTP9GkpTDOR0f1ZFF-2k-DwHXU9OYKVA3nh3zpwgINE94k-DfDHN0Mcmfog=="
    org = "primary"
    url = "http://influxdb.localdev.me"
    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    bucket="primary"
    write_api = write_client.write_api(write_options=SYNCHRONOUS)


    point = (
        Point('162_1')
        .field('cnt', int(ptli[0]))
        .field('img', str(ptli[1])),
        Point('162_2')
        .field('cnt', int(ptli[2]))
        .field('img', str(ptli[3])),
        # Point(tmps[1][0][0])
        # .field('img', tmps[1][0][1])
        # .field('cnt', int(tmps[1][0][2])),
        # Point(tmps[3][0][0])
        # .field('img', tmps[3][0][1])
        # .field('cnt', int(tmps[3][0][2])),
        )

    write_api.write(bucket=bucket, org="primary", record=point)
    time.sleep(1) # separate points by 1 second



pt = '/app/orig.jpg'
getfile(pt)
cropimg(pt)
chel = aipredict()
print('\n ##### \n')
print(chel[2])
print(chel[0])
print('\n ##### \n')
tobase(chel)
