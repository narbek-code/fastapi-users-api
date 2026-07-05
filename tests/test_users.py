import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test_pytest.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_user(db_session):
    response = client.post("/users", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_create_user_duplicate_email(db_session):
    client.post("/users", json={"name": "First", "email": "dup@example.com"})
    response = client.post("/users", json={"name": "Second", "email": "dup@example.com"})
    assert response.status_code == 400


def test_get_nonexistent_user(db_session):
    response = client.get("/users/999999")
    assert response.status_code == 404


def test_delete_user(db_session):
    create_resp = client.post("/users", json={"name": "ToDelete", "email": "delete@example.com"})
    user_id = create_resp.json()["id"]
    delete_resp = client.delete(f"/users/{user_id}")
    assert delete_resp.status_code == 204