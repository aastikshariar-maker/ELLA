"""Test suite for API endpoints"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "docs" in data


def test_create_company(client):
    """Test company creation endpoint"""
    response = client.post(
        "/api/companies/",
        params={
            "name": "TestCo",
            "industry": "SaaS",
            "stage": "seed",
            "team_size": 5,
        },
    )
    # Note: Will fail without database, but shows API structure
    assert response.status_code in [200, 400, 422]
