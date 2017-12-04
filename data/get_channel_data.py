#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python geolocation_search.py --q=surfing --location-"37.42307,-122.08427" --location-radius=50km --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
# juraszeklukasz@gmail.com
#DEVELOPER_KEY = 'AIzaSyAxE8rhzz7oFXguXew0uzi5dRP44kY-Dro'
DEVELOPER_KEY = 'AIzaSyBP1z_jkcwcgzmlGKuS4qzqxGlHx4Nbrdc'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def youtube_search(youtube, line, output):
    search_response = youtube.channels().list(
        part='statistics',
        id = line
    ).execute()
    
    if len(search_response["items"]) == 0:
        return

    for item in search_response["items"]:
        try:
            id = item["id"]
            viewCount = item["statistics"]["viewCount"]
            commentCount = item["statistics"]["commentCount"]
            subscriberCount = item["statistics"]["subscriberCount"]
            videoCount = item["statistics"]["videoCount"]

            vector = (id + "," + viewCount + "," + commentCount + "," + subscriberCount + "," + videoCount + "\n")
            output.write(vector)
        except:
            print "Some shit went down."
            return

if __name__ == '__main__':
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    file = open("channels.txt", 'r')
    output = open("channel_data.txt", 'a')
    count = 1
    for line in file:
        line = line.replace("\n", "")
        print "Channel #%d" % count
        youtube_search(youtube, line, output)
        count += 1
    file.close()
    output.close()
