from flask import Blueprint, redirect, url_for, session
from app.services.google_oauth import  oauth_flow

auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/')
# def home():
#     return redirect(url_for('auth.login'))

@auth_bp.route('/login')
def login():
    authorization_url, state = oauth_flow()
    session['state'] = state
    return redirect(authorization_url)

@auth_bp.route('/callback/google')
def callback():
    from app.services.google_oauth import handle_callback
    return handle_callback()
