from fastapi.testclient import TestClient
from app.main import app
import os
from unittest.mock import patch

client = TestClient(app)

def test_with_correct_api_key():
    with patch.dict(os.environ, {"API_KEY": "test"}):
        # Arrange
        API_KEY = os.environ.get("API_KEY")

        # Act
        response = client.get("/", headers={"X-API-Key": API_KEY})

        # Assert
        assert response.status_code != 401
    
def test_with_wrong_api_key():
    with patch.dict(os.environ, {"API_KEY": "test"}):
        # Act
        response = client.get("/", headers={"X-API-KEY": "1234"})
        
        # Assert
        assert response.status_code == 401

def test_without_api_key():
    # Act
    response = client.get("/")
    
    # Assert
    assert response.status_code == 401