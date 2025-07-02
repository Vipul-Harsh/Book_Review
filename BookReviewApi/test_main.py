from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_and_get_book():
    response = client.post("/books", json={"title": "Test Book"})
    assert response.status_code == 200
    book_id = response.json()["id"]

    response = client.get("/books")
    assert any(book["id"] == book_id for book in response.json())

def test_add_and_get_review():
    response = client.post("/books", json={"title": "Another Book"})
    book_id = response.json()["id"]
    
    response = client.post(f"/books/{book_id}/reviews", json={"review_text": "Nice book!"})
    assert response.status_code == 200

    response = client.get(f"/books/{book_id}/reviews")
    assert response.status_code == 200
