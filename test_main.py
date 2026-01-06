import json
import os
import pytest
from main import app, FILE_NAME

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def setup_function():
    # Καθαρίζουμε το αρχείο πριν από κάθε test
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def test_get_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "username": "testuser",
            "title": "Test task",
            "description": "Testing",
            "deadline": "2026-01-01"
        }
    )
    assert response.status_code == 201

def test_delete_task(client):
    # πρώτα δημιουργούμε task
    client.post(
        "/tasks",
        json={
            "username": "testuser",
            "title": "Task to delete",
            "description": "Delete me",
            "deadline": "2026-01-01"
        }
    )

    # μετά το διαγράφουμε
    response = client.delete("/tasks/1")
    assert response.status_code == 200
