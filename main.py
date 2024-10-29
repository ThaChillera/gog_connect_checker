#!/usr/bin/python3

#get rss save location from arguments
import sys
import getopt

instructions = 'test.py -r | --rss <rss file>'
rss_location = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"hr:", ["rss="])
except getopt.GetoptError:
    print(instructions, file=sys.stderr)
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print(instructions)
        sys.exit()
    elif opt in ('-r', '--rss'):
        rss_location = arg

if (not rss_location):
    print(instructions, file=sys.stderr)
    sys.exit(2)

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

rssFile = open(rss_location, 'w')
rssFile.write(feed.rss())
rssFile.close()
