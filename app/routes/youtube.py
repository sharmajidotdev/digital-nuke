from flask import Blueprint, session, render_template, redirect, url_for
from app.services.youtube_api import get_liked_videos

youtube_bp = Blueprint('youtube', __name__)

@youtube_bp.route('/liked-videos')
def liked_videos():
    if 'credentials' not in session:
        return redirect(url_for('auth.login'))

    videos = get_liked_videos(session['credentials'])
    print(f"Retrieved {len(videos)} liked videos.")
    return render_template('liked_videos.html', videos=videos)
