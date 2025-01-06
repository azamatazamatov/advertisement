from fastapi.testclient import TestClient
from app.main import app
import os
from unittest.mock import patch

client = TestClient(app)

def test_with_correct_api_key():
    with patch.dict(os.environ, {"API_KEY": "test"}):
        response = client.get("/", headers={"X-API-Key": "test"})

        assert response.status_code != 401
    
def test_with_wrong_api_key():
    with patch.dict(os.environ, {"API_KEY": "test"}):
        response = client.get("/", headers={"X-API-KEY": "1234"})
        
        assert response.status_code == 401

def test_without_api_key():
    response = client.get("/")
    
    assert response.status_code == 401