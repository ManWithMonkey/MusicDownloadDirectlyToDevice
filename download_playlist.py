#!/usr/bin/env python3

import re
from sys import argv
import random

from timeout import *
from clear import *
from cleanurl import *
from converttrash import *
from device import *
from youtubestuff import *
from config import *

if __name__ == '__main__':
    if len(argv) > 2:
        link = CleanPlaylistURL(argv[1])
        ClearAllSongs()
        ClearAllTrash()
        DownloadPlaylist(link, int(argv[2]))
        ConvertAll()
        MoveAllToDevice()
    elif len(argv) > 1:
        link = CleanPlaylistURL(''.join(argv[1:]))
        ClearAllSongs()
        ClearAllTrash()
        DownloadPlaylist(link)
        ConvertAll()
        MoveAllToDevice()
    else:
        print("Give link to playlist.")
        print("./download_playlist.py <link> <cap>")
