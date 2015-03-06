#!usr/bin/python
# Filename: memory_leak.py

import fileinfo

def leakmem():
    f = fileinfo.FileInfo('/music/_singles/kairo.mp3')

for i in range(100):
    leakmem()

class counter:
    count = 0
    def __init__(self):
        self.__class__.count += 1


