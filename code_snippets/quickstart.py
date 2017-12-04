# Sample Python code for user authorization

import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
  results = service.captions().list(
    **kwargs
  ).execute()
  
  print(results)

# Call the API's captions.list method to list the existing caption tracks.
def list_captions(youtube, video_id):
    results = youtube.captions().list(
        part="snippet",
        videoId=video_id
        ).execute()

    for item in results["items"]:
        id = item["id"]
        name = item["snippet"]["name"]
        language = item["snippet"]["language"]
        print "Caption track '%s(%s)' in '%s' language." % (name, id, language)

        return results["items"]

# Call the API's captions.download method to download an existing caption track.
def download_caption(youtube, caption_id, tfmt):
    subtitle = youtube.captions().download(
        id=caption_id,
        tfmt=tfmt
        ).execute()
    
    print "First line of caption track: %s" % (subtitle)


if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  id_num = "DPm3S6iqJxg"
  captions = list_captions(service, id_num)

  first_caption_id = captions[0]['id'];
  download_caption(service, first_caption_id, 'srt')
  print "Created and managed caption tracks."
