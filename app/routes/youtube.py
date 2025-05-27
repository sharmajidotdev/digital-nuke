from flask import Blueprint, session, render_template, redirect, url_for
from app.services.youtube_api import get_liked_videos, get_disliked_videos

youtube_bp = Blueprint('youtube', __name__)

@youtube_bp.route('/liked-videos')
def liked_videos():
    if 'credentials' not in session:
        return redirect(url_for('auth.login'))

    videos = get_liked_videos(session['credentials'])
    print(f"Retrieved {len(videos)} liked videos.")
    return render_template('liked_videos.html', videos=videos)

@youtube_bp.route('/disliked-videos')
def disliked_videos():
    if 'credentials' not in session:
        return redirect(url_for('auth.login'))

    videos = get_disliked_videos(session['credentials'])
    print(f"Retrieved {len(videos)} disliked videos.")
    return render_template('disliked_videos.html', videos=videos)

@youtube_bp.route('/subscriptions')
def subscriptions():
    if 'credentials' not in session:
        return redirect(url_for('auth.login'))

    # Placeholder for subscriptions functionality
    # Implement the logic to fetch subscriptions here
    return render_template('subscriptions.html', subscriptions=[])