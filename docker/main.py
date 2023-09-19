import datetime
import socket
import os

print ("Hello kubernetes!!!")
print("Now =", datetime.datetime.now())
print("Hostname =", socket.gethostname())
print("Home dir =", os.path.expanduser('~'))
