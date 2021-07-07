#!/usr/bin/env python3

from datetime import datetime
from random import choice

from filehelper import GetFilesInDirectory
from device import GetAllSongsOnDevice
from config import *

def LogDeviceSongs(tofile):
    print("Logging songs to:", tofile)
    files = GetAllSongsOnDevice()
    if not files:
        print("No files in device or device not connected. Not logging.")
    else:
        with open(tofile, 'w+') as f:
            for file in files:
                f.write(file[len(MUSICDST):]+"\n")

def GetYTURLBasedOnLogNode(data):
    return "???"

def GetRandomLog():
    files = GetFilesInDirectory(LOGDIR)
    file = choice(files)
    return file

def GetLogURLs(logfile):
    print("Getting log:", logfile)
    text = None
    with open(logfile, 'r') as f:
        text = f.read()

    datas = text.split()
    result = [GetYTURLBasedOnLogNode(data) for data in datas]

    return result

if __name__ == '__main__':
    now = datetime.now()
    filename = LOGDIR + str(now)+".log"
    LogDeviceSongs(filename)
