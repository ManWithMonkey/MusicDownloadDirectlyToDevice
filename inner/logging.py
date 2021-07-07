#!/usr/bin/env python3

from datetime import datetime

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

if __name__ == '__main__':
    now = datetime.now()
    filename = LOGDIR + str(now)+".log"
    LogDeviceSongs(filename)
