#!/usr/bin/env python3

from datetime import datetime
from random import choice

from filehelper import *
from device import *
from youtubestuff import *
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

def GetLogTitles(logfile):
    print("Getting log:", logfile)
    text = None
    with open(logfile, 'r') as f:
        text = f.read()
    titles = text.split('\n')
    return titles

def GetRandomLog():
    files = GetFilesInDirectory(LOGDIR)
    file = choice(files)
    return file

if __name__ == '__main__':
    now = datetime.now()
    filename = LOGDIR + str(now)+".log"
    print("Logging songs to:", filename)
    LogDeviceSongs(filename)
