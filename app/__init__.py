from flask import Flask
from app.routes.auth import auth_bp
from app.routes.youtube import youtube_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.config.from_object('app.config.Config')

    app.register_blueprint(auth_bp)
    app.register_blueprint(youtube_bp)

    return app
