from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_liked_videos(session_creds):
    creds = Credentials(**session_creds)
    youtube = build('youtube', 'v3', credentials=creds)

    videos = []
    next_page_token = None

    while True:
        request = youtube.videos().list(
            part="snippet,contentDetails",
            myRating="like",
            maxResults=50,  # maximum allowed by API
            pageToken=next_page_token
        )
        response = request.execute()
        videos.extend(response.get('items', []))
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos