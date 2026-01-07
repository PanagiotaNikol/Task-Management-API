import json
import os
import pytest
from main import app, FILE_NAME

# Δημιουργία test client για το Flask app
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# Καθαρίζει το αρχείο tasks.txt πριν από κάθε test
def setup_function():
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

# Έλεγχος ότι αρχικά δεν υπάρχουν tasks
def test_get_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []

# Έλεγχος δημιουργίας νέου task
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

# Έλεγχος διαγραφής ενός task
def test_delete_task(client):
    # πρώτα δημιουργούμε task για να το διαγράψουμε
    client.post(
        "/tasks",
        json={
            "username": "testuser",
            "title": "Task to delete",
            "description": "Delete me",
            "deadline": "2026-01-01"
        }
    )

    # διαγραφή task με id 1
    response = client.delete("/tasks/1")
    assert response.status_code == 200

