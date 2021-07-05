#!/usr/bin/env python3

import re
from pytube import Playlist
from sys import argv
from timeout import timeout

from clear import ClearAllTrash, ClearAllSongs
from cleanurl import CleanURL
from converttrash import ConvertAll
from movetodevice import MoveAllToDevice

from config import *

def DownloadPlaylist(link):
    print("Downloading playlist:", link)
    playlist = Playlist(link)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print("Found:", len(playlist.video_urls))

    for url in playlist.video_urls:
        print(url)

    @timeout(DOWNLOAD_DELAY)
    def DownloadVideo(video):
        print("Downloading:", "\""+video.title+"\"", "to", TRASHDIR)
        audio = video.streams.get_by_itag('140')
        audio.download(output_path=TRASHDIR)

    for video in playlist.videos:
        try:
            DownloadVideo(video)
        except:
            continue

if __name__ == '__main__':
    if len(argv) > 1:
        link = CleanURL(''.join(argv[1:]))

        ClearAllSongs()
        ClearAllTrash()
        DownloadPlaylist(link)
        ConvertAll()
        MoveAllToDevice()
    else:
        print("Give link to playlist")
