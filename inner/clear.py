#!/usr/bin/env python3

import os
import glob

from config import *

def ClearAllSongs():
    files = glob.glob(MUSICSRC+"*.mp3")
    for f in files:
        os.remove(f)

def ClearAllTrash():
    files = glob.glob(TRASHDIR+"*.mp4")
    for f in files:
        os.remove(f)

if __name__ == '__main__':
    ClearAllSongs()
    ClearAllTrash()