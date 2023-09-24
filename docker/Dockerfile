# Задаём имя базового образа, в котором есть интерпретатор Python 
FROM python

# builder-base is used to build dependencies
RUN apt-get update && apt-get upgrade -y \ 
        && apt-get install --no-install-recommends -y \
        curl \
        vim

RUN mkdir /app 
# Назначаем рабочую директорию
WORKDIR /app
# Добавляем скрипт в файловую систему образа
RUN pip3 install --upgrade pip
RUN pip3 install minio requests boto3 ultralytics imgaug influxdb-client opencv-python defisheye
#RUN pip3 install ultralytics imgaug influxdb-client opencv-python defisheye
#RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Для обеспечения безопасности переключаем пользователя на непривилигированного
ADD ./*.py ./

#USER 1001