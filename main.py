#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup

#download list of games
root = BeautifulSoup(urllib.request.urlopen('http://gog.com/connect').read().decode('utf-8'), 'html.parser')

games = set()

for game in root.find_all('span'):
    classvalue = game.get('class')
    if (classvalue and classvalue[0] == 'product-title__text' and game.string):
        games.add(game.string)

# generate RSS feed

import datetime
from rfeed.rfeed import *

feedItems = []

for game in games:
    feedItems.append(Item(
    title = game,
    link = "http://www.gog.com/connect", 
    description = game,
    guid = Guid("http://www.gog.com/connect/" + game.replace(' ', '')),
    pubDate = datetime.datetime.now(datetime.timezone.utc)))

feed = Feed(
    title = "GoG Connect Feed",
    link = "http://www.example.com/rss",
    description = "This is a feed of all GoG connect games",
    language = "en-US",
    lastBuildDate = datetime.datetime.now(),
    items = feedItems)

rssFile = open('rss.xml', 'w')
rssFile.write(feed.rss())
rssFile.close()
