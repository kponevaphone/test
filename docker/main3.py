import  os, time, base64, requests, shutil, random, uuid, datetime, socket

with open('/etc/hosts', 'a') as f:
    f.write('192.168.243.10    minio.localdev.me\n')
    f.write('192.168.243.10    influxdb.localdev.me\n')
 
print ("Hello 3 from kubernetes!!!")
print("datetime now =", datetime.datetime.now())
print("Hostname =", socket.gethostname())
