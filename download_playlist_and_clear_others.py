#!/usr/bin/env python3

import re
from pytube import Playlist
from sys import argv

from inner import clear, cleanurl, converttrash, movetodevice

from inner.timeout import timeout
from inner.clear import ClearAllTrash, ClearAllSongs
from inner.cleanurl import CleanURL
from inner.converttrash import ConvertAll
from inner.movetodevice import MoveAllToDevice

from config import *

def DownloadPlaylist(link, link_cap = None):
    print("Downloading playlist:", link)
    playlist = Playlist(link)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print("Found:", len(playlist.video_urls), "link(s) and downloading:", (link_cap if link_cap else len(playlist.video_urls)))

    for url in playlist.video_urls[:link_cap if link_cap else len(playlist.video_urls)]:
        print(url)

    @timeout(DOWNLOAD_DELAY)
    def DownloadVideo(video, msg):
        print(msg)
        audio = video.streams.get_by_itag('140')
        audio.download(output_path=TRASHDIR)

    MAX_ATTEMPTS = 2
    for video in playlist.videos[:link_cap if link_cap else len(playlist)]:
        for attempt in range(MAX_ATTEMPTS):
            try:
                msg = ("Downloading: \"" if attempt == 0 else "Attempting to download again: \"") + video.title + "\" to " + TRASHDIR
                DownloadVideo(video, msg)
                break
            except:
                continue

if __name__ == '__main__':
    if len(argv) > 2:
        # link = CleanURL(argv[1])
        # ClearAllSongs()
        # ClearAllTrash()
        # DownloadPlaylist(link, int(argv[2]))
        # ConvertAll()
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
        print("./download_playlist_and_clear_others.py <link> <cap>")