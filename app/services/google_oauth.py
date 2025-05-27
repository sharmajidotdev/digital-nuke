import requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
import os
from flask import url_for, session, redirect

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

def oauth_flow():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/youtube.readonly', 'openid', 'email', 'profile']
    )
    flow.redirect_uri = url_for('auth.callback', _external=True)
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    return authorization_url, state

def handle_callback():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/youtube.readonly', 'openid', 'email', 'profile']
    )
    flow.redirect_uri = url_for('auth.callback', _external=True)

    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)
    return redirect(url_for('youtube.liked_videos'))

def credentials_to_dict(creds):
    return {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'token_uri': creds.token_uri,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret,
        'scopes': creds.scopes
    }
