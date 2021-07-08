#!/usr/bin/env python3

import re
from sys import argv

def CleanPlaylistURL(url):
    pattern="(watch.+?(?=list)|&index.+|&start_radio.+)"
    prog = re.compile(pattern)
    results = prog.findall(url)
    text = url
    if len(results) > 0:
        text = text.replace(results[0], 'playlist?')
    if len(results) > 1:
        for r in results[1:]:
            text = text.replace(r, '')
    return text

if __name__ == "__main__":
    url = CleanPlaylistURL(argv[1])
    print(url)
