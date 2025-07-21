import pytest
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from app import create_app, db
except ImportError:
    try:
        from main import create_app, db
    except ImportError:
        try:
            from application import create_app, db
        except ImportError:
            # Fallback for basic Flask apps
            from flask import Flask
            
            def create_app():
                app = Flask(__name__)
                app.config.update({
                    "TESTING": True,
                    "SECRET_KEY": "test-secret-key"
                })
                return app
            
            db = None

@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SECRET_KEY": "test-secret-key",
        "WTF_CSRF_ENABLED": False,
    })
    
    # Add database configuration if db exists
    if db is not None:
        app.config.update({
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False
        })
        
        with app.app_context():
            db.create_all()
            yield app
            db.drop_all()
    else:
        yield app

@pytest.fixture()
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture()
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

@pytest.fixture()
def auth_headers():
    """Common authentication headers for testing."""
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer test-token'
    }
