#!/usr/bin/env python3

import os
from os import listdir
from os.path import isfile, join
import glob
import subprocess

from config import *

def GetFilesInDirectory(dirpath):
    return [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

def GetAllSongsOnDevice():
    return glob.glob(MUSICDST+"*.mp3")

def ClearDevice():
    oldFiles = glob.glob(MUSICDST+"*.mp3")
    for f in oldFiles:
        os.remove(f)

def MoveAllToDevice():
    for f in GetFilesInDirectory(MUSICSRC):
        src = MUSICSRC + f
        dst = MUSICDST + f[:-4] + ".mp3"
        print("Moving file:", f)
        
        cmd = "cp \"" + src + "\" \"" + dst + "\""
        subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    MoveAllToDevice()
