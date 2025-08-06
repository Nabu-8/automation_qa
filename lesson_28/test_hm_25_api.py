import requests
import pytest
from lesson_28.users_data import random_email

@pytest.mark.api
def test_successful_registration_api():
    url = "https://qauto2.forstudy.space/api/auth/signup"

    email = random_email()
    payload = {
        "name": "Test",
        "lastName": "User",
        "email": email,
        "password": "Pass1234",
        "repeatPassword": "Pass1234"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}, response: {response.text}"
    json_data = response.json()
    assert json_data["status"] == "ok"


@pytest.mark.hw25()
@pytest.mark.negative
@pytest.mark.api
def test_user_already_exists_api(registered_user_email):
    url = "https://qauto2.forstudy.space/api/auth/signup"
    payload = {
        "name": "Test",
        "lastName": "User",
        "email": registered_user_email,
        "password": "Pass1234",
        "repeatPassword": "Pass1234"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 400
    assert response.json()["status"] == "error"
    assert response.json()["message"] == "User already exists"