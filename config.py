# App configuration (database, secrets, etc.)
import os
from datetime import timedelta
from dotenv import load_dotenv

# Load .env file into environment variables
load_dotenv()

class Config:
    """Base configuration - shared by all environments."""
    
    # Secret key for session encryption (from .env)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-dev-key')
    
    # Database connection string (from .env)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    # Disable Flask-SQLAlchemy event tracking (saves memory)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT settings
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)