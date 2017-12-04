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
DEVELOPER_KEY = 'AIzaSyAxE8rhzz7oFXguXew0uzi5dRP44kY-Dro'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(youtube):
    ids_count = 0
    pt = ''
    
    results = []

    while (ids_count < 100000):

        search_response = youtube.search().list(
            part='snippet',
            maxResults = 50,
            type = 'video',
            pageToken = pt,
            regionCode = 'US'
            #relevanceLanguage = 'en'
        ).execute()
        
        if len(search_response["items"]) == 0:
            print "Response returned 0 ids"

        for item in search_response["items"]:
            try:
                id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                channel = item["snippet"]["channelId"]
                description = item["snippet"]["description"]
                vector = id + ", " + channel + ", " + title + ", "  + ", (" + description + "),"
                vector = ''.join([i if ord(i) < 128 else '' for i in vector])
                results.append(vector)
                ids_count += 1
            except:
                continue
        pt = search_response["nextPageToken"]
        print "Next Page Token ", pt
        print("Currently, we have " + str(ids_count) + " video ids.")

    return results
if __name__ == '__main__':
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    file = open("video_ids.txt", 'w')
    results = youtube_search(youtube)
    for each in results:
        file.write(each + "\n")
    file.close()
