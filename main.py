#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup

f = open("output.html", 'w')

content = urllib.request.urlopen('http://gog.com/connect').read().decode('utf-8')
f.write(content)
f.close()

root = BeautifulSoup(content, 'html.parser')

games = set()

for game in root.find_all('span'):
    classvalue = game.get('class')
    if (classvalue and classvalue[0] == 'product-title__text' and game.string):
        games.add(game.string)

print(games)
