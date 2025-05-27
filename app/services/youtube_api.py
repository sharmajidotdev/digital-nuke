from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_liked_videos(session_creds):
    creds = Credentials(**session_creds)
    youtube = build('youtube', 'v3', credentials=creds)

    request = youtube.videos().list(
        part="snippet,contentDetails",
        myRating="like"
    )
    response = request.execute()

    return response.get('items', [])
