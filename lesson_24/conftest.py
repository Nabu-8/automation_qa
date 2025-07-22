import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass"))
    response.raise_for_status()
    access_token = response.json()["access_token"]
    session.headers.update({'Authorization': f'Bearer {access_token}'})
    return session


@pytest.fixture(scope="class")
def total_cars_count(auth_session):
    response = auth_session.get(f"{BASE_URL}/cars", params={"limit": 1000})
    response.raise_for_status()
    data = response.json()
    return len(data)