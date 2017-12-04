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

def youtube_search(youtube, line, output, channels):

    # Call the search.list method to retrieve results matching the specified
    # query term.
  

    search_response = youtube.videos().list(
        part='snippet',
        id = line
    ).execute()
    
    
    if len(search_response["items"]) == 0:
        return

    if not isEnglish(search_response["items"][0]["snippet"]["title"]):
        print "Not english"
        return

    for item in search_response["items"]:
        try:
            id = item["id"]
            title = item["snippet"]["title"]
            title.replace(",", "")
            channel = item["snippet"]["channelId"]
            category = item["snippet"]["categoryId"]
            tags = []
            if "tags" in item["snippet"]:
                tags = item["snippet"]["tags"]
            for i in range(len(tags)):
                tags[i] = tags[i].replace("\n", "")
            vector = (id + ", " + channel + ", " + title + ", " + category + ", (" + ','.join(tags) + "), " + "\n")
            vector = ''.join([i if ord(i) < 128 else '' for i in vector])
            channels.write(str(channel))
            output.write(vector)
        except:
            print "Some shit went down."
            return

if __name__ == '__main__':
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    file = open("video_ids.txt", 'r')
    output = open("my_data.txt", 'w')
    channels = open("channels.txt", 'w')
    count = 1
    for line in file:
        print "Video #%d" % count
        youtube_search(youtube, line, output, channels)
        count += 1
    file.close()
    output.close()
    channels.close()
