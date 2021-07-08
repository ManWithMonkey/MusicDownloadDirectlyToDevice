#!/usr/bin/env python3

import re
import random

from pytube import Playlist, YouTube
from youtubesearchpython import VideosSearch

from config import *

def GetLinksByTitle(title, limit=3):
    print("Searching link(s) with title: ", title)
    results = VideosSearch(title, limit=limit).result()
    return [x['link'] for x in results['result']]

def GetLinkByTitle(title):
    links = GetLinksByTitle(title, 1)
    return links[0]

def GetUrlForTitle(title):
    return GetLinkByTitle(title)

def DownloadVideo(link):
    print("Downloading video: ", link)
    vid = YouTube(link)
    t = vid.streams.filter(only_audio=True)
    t[0].download(TRASHDIR)

def DownloadPlaylist(link, link_cap = None):
    print("Downloading playlist:", link)
    playlist = Playlist(link)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    videos, urls = list(zip(*(sorted(zip(playlist.videos, playlist.video_urls), key=lambda _: random.random()))[:link_cap if link_cap else len(playlist)]))

    print("Found:", len(playlist.videos), "link(s) and downloading:", len(urls))
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