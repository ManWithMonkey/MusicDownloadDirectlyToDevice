#!/usr/bin/env python3

import os
from sys import argv
from pytube import YouTube
import subprocess
import glob

def filenameFromFilepath(filepath):
    return filepath[filepath.rfind('/')+1:]

while True:
    url = input("Paste URL: ")
    yt=YouTube(url)
    t=yt.streams.filter(only_audio=True)
    t[0].download("./trash/")

    oldFiles = glob.glob("./trash/*.mp4")
    for f in oldFiles:    
        mp4 = "\"" + f + "\""
        mp3 = "\"./songs/" + (filenameFromFilepath(f))[:-4] +'.mp3' + "\""
        ffmpeg = "ffmpeg -y -i " + mp4 + " " + mp3
        print(ffmpeg)
        subprocess.call(ffmpeg, shell=True)
        os.remove(f)
