import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Now import should work

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
