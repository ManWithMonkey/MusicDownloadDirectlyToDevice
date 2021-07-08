#!/usr/bin/env python3

import subprocess
import glob

from config import *

def FilenameFromPath(filepath):
    return filepath[filepath.rfind('/')+1:]

def ConvertAll():
    files = glob.glob(TRASHDIR+"*.mp4")
    for f in files:
        mp4 = "\"" + f + "\""
        mp3 = "\"" + MUSICSRC + (FilenameFromPath(f))[:-4] +'.mp3' + "\""
        cmd = "ffmpeg -y -i " + mp4 + " " + mp3 + " -nostats -loglevel 0"
        print("Converting", mp4, "to", mp3)
        # print(cmd)
        subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    ConvertAll()
