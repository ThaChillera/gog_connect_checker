# GoG Gonnect Checker
Script to get all games from GoG connect, and add to/update an rss file

## Requirements
  * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

## How to use:
The program requires a location argument (-r or --rss) to know where the rss output should be stored.
Intended functionality is for the previous file to be read and updated as needed, to create a valid RSS feed.

The script should rune periodically (every 24 hours) to keep track of what games are available

# TODO:
  * ~~Update existing RSS file instead of re-making from scratch~~
  * Create Docker File
    * RSS Location passed by ENV variable
    * Runs script every time docker is run
  * Add way to specify feed URL
