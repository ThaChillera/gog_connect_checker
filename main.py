#!/usr/bin/python3

# if env has been set, use as location
import os
rss_location = ''
if os.environ['RSS_LOCATION'] :
	rss_location = os.environ['RSS_LOCATION']

# get rss save location from arguments
if not rss_location :
    import sys
    import getopt
    
    instructions = 'test.py -r | --rss <rss file> | $RSS_LOCATION'
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
import datetime

# download list of games
root = BeautifulSoup(urllib.request.urlopen('http://gog.com/connect').read().decode('utf-8'), 'html.parser')

# dict: key = game title, value = retrieval date
games = dict()

for game in root.find_all('span'):
    classvalue = game.get('class')
    if (classvalue and classvalue[0] == 'product-title__text' and game.string):
        games[game.string] = datetime.datetime.now()

# make sure existing results are updated, not overwritten
import os.path
import feedparser

if os.path.isfile(rss_location):
    newsfeed = feedparser.parse(rss_location)
    for entry in newsfeed.entries:
        if entry.title in games:
            date = datetime.datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
            games[entry.title] = date

# generate RSS feed
from rfeed.rfeed import *

feedItems = []

for game, date in games.items():
    feedItems.append(Item(
    title = game,
    link = "http://www.gog.com/connect", 
    description = game,
    guid = Guid("http://www.gog.com/connect/" + game.replace(' ', '')),
    pubDate = date
    ))

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
