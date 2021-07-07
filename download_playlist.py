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

from inner.config import *

def DownloadPlaylist(link, link_cap = None):
    print("Downloading playlist:", link)
    playlist = Playlist(link)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    videos, urls = list(zip(*(sorted(zip(playlist.videos, playlist.video_urls), key=lambda _: random.random()))[:link_cap if link_cap else len(playlist)]))

    print("Found:", len(urls), "link(s) and downloading:", len(urls))
    for url in urls:
        print(url)

    @timeout(DOWNLOAD_DELAY)
    def DownloadVideo(video, msg):
        print(msg)
        audio = video.streams.get_by_itag('140')
        audio.download(output_path=TRASHDIR)

    MAX_ATTEMPTS = 2
    for video in videos:
        for attempt in range(MAX_ATTEMPTS):
            try:
                msg = ("Downloading: \"" if attempt == 0 else "Attempting to download again: \"") + video.title + "\" to " + TRASHDIR
                DownloadVideo(video, msg)
                break
            except:
                continue

if __name__ == '__main__':
    if len(argv) > 2:
        link = CleanURL(argv[1])
        ClearAllSongs()
        ClearAllTrash()
        DownloadPlaylist(link, int(argv[2]))
        ConvertAll()
        MoveAllToDevice()
    elif len(argv) > 1:
        link = CleanURL(''.join(argv[1:]))
        ClearAllSongs()
        ClearAllTrash()
        DownloadPlaylist(link)
        ConvertAll()
        MoveAllToDevice()
    else:
        print("Give link to playlist.")
        print("./download_playlist.py <link> <cap>")
