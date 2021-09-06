from fastapi.testclient import TestClient

from backend.portfolio_website.app.api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to your todo list."}
