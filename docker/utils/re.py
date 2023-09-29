import os


#!/usr/bin/env python3

# Импорт модуля uuid 
from random import randint

# Создание случайного идентификатора с помощью uuid1()

dirlist = []
# определение текущей рабочей директории
path = os.getcwd()
# чтение записей
with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        # печать всех записей, являющихся файлами
        if entry.is_file():
            if entry.name.endswith('.jpeg'):
                old_name = f'{path}\{entry.name}'
                new_name = f'{path}\{randint(19999999, 99999999)}.jpg'
                os.rename(old_name, new_name)

print(dirlist)
for _ in dirlist:
    print(_)
    
# import os

# # Absolute path of a file
# old_name = r"E:\demos\files\reports\details.txt"
# new_name = r"E:\demos\files\reports\new_details.txt"

# # Renaming the file
# os.rename(old_name, new_name)