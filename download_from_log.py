#!/usr/bin/env python3

import re
from pytube import Playlist
from sys import argv
import random

from timeout import *
from clear import *
from cleanurl import *
from converttrash import *
from device import *
from logs import *
from config import *

def DownloadFromLog(logfile, link_cap = None):
    print("Downloading from log:", logfile)

    titles = GetLogTitles(logfile)
    count = len(titles)
    chooseCount = (link_cap if link_cap else len(titles))

    print("Found:", count, "link(s) and downloading:", chooseCount)
    print("Searching links...")
    titles = (sorted(titles, key=lambda _: random.random()))[:chooseCount]
    urls = [GetUrlForTitle(title) for title in titles]

    DownloadVideos(urls)

if __name__ == '__main__':
    if len(argv) > 2:
        ClearAllSongs()
        ClearAllTrash()
        DownloadFromLog(argv[1], int(argv[2]))
        ConvertAll()
        ClearDevice()
        MoveAllToDevice()
    elif len(argv) > 1:
        ClearAllSongs()
        ClearAllTrash()
        DownloadFromLog(argv[1], int(argv[2]))
        ConvertAll()
        ClearDevice()
        MoveAllToDevice()
    else:
        print("Give logfile location:")
        print("./dowload_from_log.py <logfile> <cap>")
