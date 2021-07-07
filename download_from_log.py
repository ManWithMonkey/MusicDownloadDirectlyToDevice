#!/usr/bin/env python3

import re
from pytube import Playlist
from sys import argv
import random

from inner import config, clear, cleanurl, converttrash, device

from inner.timeout import timeout
from inner.clear import ClearAllTrash, ClearAllSongs
from inner.cleanurl import CleanURL
from inner.converttrash import ConvertAll
from inner.device import MoveAllToDevice
from inner.log import GetRandomLogURLs

from inner.config import *

def DownloadFromLog(logfile, link_cap = None):
    print("Downloading from log:", link)

    urls = GetLogUrls(logfile)

    print("Found:", len(urls), "link(s) and downloading:", len(urls))
    for url in urls:
        print(url)

    # do something

if __name__ == '__main__':
    # if len(argv) > 2:
    #     link = CleanURL(argv[1])
    #     ClearAllSongs()
    #     ClearAllTrash()
    #     DownloadPlaylist(link, int(argv[2]))
    #     ConvertAll()
    #     MoveAllToDevice()
    # elif len(argv) > 1:
    #     link = CleanURL(''.join(argv[1:]))
    #     ClearAllSongs()
    #     ClearAllTrash()
    #     DownloadPlaylist(link)
    #     ConvertAll()
    #     MoveAllToDevice()
    # else:
    #     print("Give link to playlist.")
    #     print("./download_playlist.py <link> <cap>")
    pass
