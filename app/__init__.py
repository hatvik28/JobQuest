# Flask app factory will go here
from flask import Flask

def create_app():
    """Application factory - creates and configures the Flask app."""
    app = Flask(__name__)
    
    # Simple test route
    @app.route('/')
    def home():
        return {'message': 'Job Tracker API is running!'}
    
    return app