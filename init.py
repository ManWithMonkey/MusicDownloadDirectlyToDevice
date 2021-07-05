#!/usr/bin/env python3

import os

this_dir = os.path.dirname(os.path.abspath(__file__))

CONFIGFILE = this_dir + "/config.py"

if not os.path.exists(CONFIGFILE):
    print("Creating config file:", CONFIGFILE)

TRASHDIR = this_dir + "/trash/"
MUSICSRC = this_dir + "/songs/"

if not os.path.exists(TRASHDIR):
    print("Creating:", TRASHDIR)
    os.mkdir(TRASHDIR)
if not os.path.exists(MUSICSRC):
    print("Creating:", MUSICSRC)
    os.mkdir(MUSICSRC)

MUSICDST = input("Enter music destination folder: ")
if(MUSICDST[-1] != '/'):
    MUSICDST += '/'

DOWNLOAD_DELAY = 10

with open(CONFIGFILE, "w+") as f:
    f.write(f"{TRASHDIR=}\n")
    f.write(f"{MUSICSRC=}\n")
    f.write(f"{MUSICDST=}\n")
    f.write(f"{DOWNLOAD_DELAY=}\n")
