import  os, time, base64, requests, shutil, random, boto3, uuid, datetime
from botocore.client import Config
from requests.auth import HTTPDigestAuth
from defisheye import Defisheye
# Importing Image class from PIL module
from PIL import Image
 
path="picture.jpeg"
pt0="0.jpeg"
Image.open(path).convert('RGB').save(pt0)
Image.open(pt0).crop((215, 565, 535, 885)).save('1.jpg')
Image.open('1.jpg').resize((640, 640)).save('1.jpg')

Image.open(pt0).crop((520, 420, 1160, 1060)).save('2.jpg')

Image.open(pt0).crop((1160, 420, 1480, 1060)).save('3.jpg')
im1 = Image.open('bg.jpg')
im2 = Image.open('3.jpg')
im1.paste(im2, (160, 0))
im1.save('3.jpg')

Image.open(pt0).crop((1480, 590, 1800, 910)).save('4.jpg')
Image.open('4.jpg').resize((640, 640)).save('4.jpg')
