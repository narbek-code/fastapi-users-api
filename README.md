# FastAPI Users API

🔗 **Live Demo**: https://fastapi-users-api-1w55.onrender.com/docs

⚠️ *Hosted on Render free tier — first request after inactivity may take 30-50 seconds to wake up.*

A minimal REST API for managing users built with **FastAPI**, **SQLite**, and **SQLAlchemy**.

## Features

- CRUD endpoints for users (`name`, `email`)
- SQLite persistence with SQLAlchemy ORM
- Automatic OpenAPI docs (`/docs`, `/redoc`)
- Unit tests with pytest

## Project Structure
```
fastapi-users-api/
├── app/
│   ├── main.py         # FastAPI application factory
│   ├── database.py     # Database engine + session dependency
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic schemas
│   ├── crud.py         # Data access helpers
│   └── routes.py       # API routes
├── tests/
│   └── test_users.py   # Unit tests
├── requirements.txt
├── conftest.py
└── README.md
```

## Prerequisites

- Python 3.11+ (works with 3.10+)

## Install dependencies

Use a virtual environment for isolation:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the server

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`
Interactive docs: `http://127.0.0.1:8000/docs`

## Run tests

```bash
pytest tests/ -v
```

## API quickstart

Create a user:
```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Ada Lovelace", "email": "ada@example.com"}'
```

List users:
```bash
curl http://127.0.0.1:8000/users
```

Get a user:
```bash
curl http://127.0.0.1:8000/users/1
```
