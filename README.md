# FastAPI Users API

A minimal production-style REST API for managing users built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

## Features
- CRUD endpoints for users (`name`, `email`)
- PostgreSQL persistence with SQLAlchemy ORM
- Environment-based configuration using `.env`
- Automatic OpenAPI docs (`/docs`, `/redoc`)

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
├── requirements.txt
├── .env.example
└── README.md
```

## Prerequisites
- Python 3.11+ (works with 3.10+)
- PostgreSQL 13+ running locally or accessible via network

## Environment variables
Copy the example file and adjust values to your setup:
```bash
cp .env.example .env
```

Key variable:
- `DATABASE_URL`: e.g. `postgresql://postgres:postgres@localhost:5432/fastapi_users_db`

## Start PostgreSQL (example with Docker)
```bash
docker run --name fastapi-users-db -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=fastapi_users_db -d postgres:16
```

## Install dependencies
Use a virtual environment for isolation:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run the server
```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`  
Interactive docs: `http://127.0.0.1:8000/docs`

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

Delete a user:
```bash
curl -X DELETE http://127.0.0.1:8000/users/1
```

## Notes
- Tables are created automatically on application start. For production, consider managing schema with Alembic migrations.
- Update `DATABASE_URL` to point to your managed PostgreSQL instance when deploying.
