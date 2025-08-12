import requests
import pytest
from lesson_28.users_data import random_email
from lesson_28.utils import build_signup_payload

url = "https://qauto2.forstudy.space/api/auth/signup"

@pytest.mark.hw25()
@pytest.mark.positive
@pytest.mark.api
def test_successful_registration_api():
    payload = build_signup_payload(random_email())
    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}, response: {response.text}"
    json_data = response.json()
    assert json_data["status"] == "ok"

@pytest.mark.hw25()
@pytest.mark.negative
@pytest.mark.api
def test_user_already_exists_api(registered_user_email):
    payload = build_signup_payload(registered_user_email)
    response = requests.post(url, json=payload)

    assert response.status_code == 400
    assert response.json()["status"] == "error"
    assert response.json()["message"] == "User already exists"