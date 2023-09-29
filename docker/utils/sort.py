import os
import shutil
from random import randint

dirlist0 = []
dirlist1 = []
dirlist2 = []
dirlist3 = []
dirlist4 = []
dirlist5 = []

# определение текущей рабочей директории
path = os.getcwd()
# чтение записей
with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        # печать всех записей, являющихся файлами
        if entry.is_file():
            if entry.name.endswith('_0.jpg'):
                shutil.move(f'{path}\{entry.name}', f'{path}\\0\{entry.name}')
            if entry.name.endswith('_1.jpg'):
                shutil.move(f'{path}\{entry.name}', f'{path}\\1\{entry.name}')
            if entry.name.endswith('_2.jpg'):
                shutil.move(f'{path}\{entry.name}', f'{path}\\2\{entry.name}')
            if entry.name.endswith('_3.jpg'):
                shutil.move(f'{path}\{entry.name}', f'{path}\\3\{entry.name}')
            if entry.name.endswith('_4.jpg'):
                shutil.move(f'{path}\{entry.name}', f'{path}\\4\{entry.name}')
            else:
                shutil.move(f'{path}\{entry.name}', f'{path}\\5\{entry.name}')
 
