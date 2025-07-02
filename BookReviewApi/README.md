# 📚 Book Review Management API

Developed by **Vipul Harsh**, this is a backend API for managing books and their reviews using FastAPI, SQLAlchemy, and SQLite. It follows a clean, modular structure and includes simple caching.

## 🚀 Features

- Add new books
- View all available books
- Add reviews to books
- View reviews for specific books
- Basic in-memory caching for improved performance
- Clean, modular project structure
- Includes unit tests with Pytest

## 🧰 Tech Stack

- FastAPI - Fast web framework
- SQLAlchemy - ORM for database handling
- SQLite - Lightweight database
- In-memory Caching - Simple dictionary-based caching
- Pytest - Testing framework
- Uvicorn - ASGI server for FastAPI

## 📦 Installation and Setup

Clone the repository:
git clone <your-repo-url>
cd BookReviewAPI

Create and activate a virtual environment:
python -m venv venv

For Windows:
venv\Scripts\activate

For Mac/Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

## 🏃 Running the Server

Start the API using:
uvicorn main:app --reload

Access the API at:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

Redoc Documentation:
http://127.0.0.1:8000/redoc

## ✅ Running Tests

To run unit tests:
pytest

## 🗂️ Project Structure

BookReviewAPI/
├── main.py            # Application entry point
├── models.py          # SQLAlchemy models
├── schemas.py         # Pydantic schemas
├── crud.py            # Business logic
├── database.py        # Database setup
├── cache.py           # In-memory cache logic
├── test_main.py       # Pytest test cases
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation

## 👨‍💻 About the Developer

Created by **Vipul Harsh** for learning, practice, and demonstration purposes. You can enhance this project with:

- Redis for scalable caching
- Alembic for database migrations
- JWT-based authentication
- Docker containerization
