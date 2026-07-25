import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "backend"))

from app import app

def test_home():

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

def test_flights():

    client = app.test_client()

    response = client.get("/flights")

    assert response.status_code == 200

def test_controllers():

    client = app.test_client()

    response = client.get("/controllers")

    assert response.status_code == 200

def test_create_task():

    client = app.test_client()

    response = client.post(
        "/tasks/create",
        data={
            "title": "Pytest Task",
            "priority": "HIGH",
            "status": "PENDING",
            "flight_id": 1,
            "controller_id": 1
        },
        follow_redirects=True
    )

    assert response.status_code == 200
