import pytest
from src.app import app

# filepath: /workspaces/python-webapp/test_app.py

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Test if home page returns 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

def test_home_message(client):
    """Test if home page returns correct message."""
    response = client.get('/')
    assert b"Hello, Welcome to Season 2! You are learning GitHub Actions." in response.data

def test_invalid_route(client):
    """Test if invalid route returns 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_response_type(client):
    """Test if response type is text/html."""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'