#!/usr/bin/env python3

from youtubesearchpython import VideosSearch
import pprint as pp

videosSearch = VideosSearch('gay', limit = 5)

res = videosSearch.result()['result']

# for l in res:
#     print("here:")
#     print(l)

links, titles = zip(*[(l['link'], l['title']) for l in res])

print(links)
print(titles)