import  os, time, base64, requests, shutil, random, boto3, uuid, datetime, re, regex, tarfile, os.path
from botocore.client import Config
from requests.auth import HTTPDigestAuth
from defisheye import Defisheye
# Importing Image class from PIL module
from PIL import Image

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

# Создание случайного идентификатора с помощью uuid1()

dirlist = []
# определение текущей рабочей директории
# path = os.getcwd()
path = "/app/img"
# чтение записей
with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        # печать всех записей, являющихся файлами
        if entry.is_file():
            if entry.name.endswith('.jpg'):
                dirlist.append(f'{path}/{entry.name}')


for dl in dirlist:
    print(dl)
    cropimg(dl)

with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        # печать всех записей, являющихся файлами
        if entry.is_file():
            if entry.name.endswith('_0.jpg'):
                shutil.move(f'{path}/{entry.name}', f'{path}/0/{entry.name}')
            if entry.name.endswith('_1.jpg'):
                shutil.move(f'{path}/{entry.name}', f'{path}/1/{entry.name}')
            if entry.name.endswith('_2.jpg'):
                shutil.move(f'{path}/{entry.name}', f'{path}/2/{entry.name}')
            if entry.name.endswith('_3.jpg'):
                shutil.move(f'{path}/{entry.name}', f'{path}/3/{entry.name}')
            if entry.name.endswith('_4.jpg'):
                shutil.move(f'{path}/{entry.name}', f'{path}/4/{entry.name}')
            if len(entry.name) == 12:
                shutil.move(f'{path}/{entry.name}', f'{path}/5/{entry.name}')



def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

make_tarfile('myimg.tar.gz', path)