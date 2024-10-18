from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)

    # Configure SQLite database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the app with the database
    db.init_app(app)

    return app
