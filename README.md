# GoG Gonnect Checker
Script to get all games from GoG connect, and add to/update an rss file

## Requirements
  * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
  * [Feedparser](https://pythonhosted.org/feedparser/)

## How to use:
The program requires a location argument (-r or --rss) to know where the rss output should be stored.
Intended functionality is for the previous file to be read and updated as needed, to create a valid RSS feed.

The script should rune periodically (every 24 hours) to keep track of what games are available

### Environment variables:
  * RSS_LOCATION: specifies the location the output should be saved
  * FEED_URL: specify the feed source URL. defaults to github repo link

## Docker
The run command results is the file feed.rss being generated into the /tmp folder.
The save location is fed via the $RSS_LOCATION environment variable

`docker run -e "RSS_LOCATION=/rss/feed.rss" -e "FEED_URL=github.com/thachillera/gog_connect_checker" -v /tmp/rss:/rss --rm thachillera/gogconnect:latest`

# TODO:
  * ~~Update existing RSS file instead of re-making from scratch~~
  * ~~Create Docker File~~
    * ~~RSS Location passed by ENV variable~~
  * ~~Add way to specify feed URL~~
