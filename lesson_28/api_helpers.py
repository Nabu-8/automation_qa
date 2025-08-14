import requests
import allure
from lesson_28.utils import build_signup_payload

url = "https://qauto2.forstudy.space/api/auth/signup"

@allure.step("Send sign up request with email: {email}")
def send_signup_request(email):
    payload = build_signup_payload(email)
    return requests.post(url, json=payload)

@allure.step("Validate response for successful registration")
def validate_successful_response(response):
    assert response.status_code == 201, f"Expected 201, got {response.status_code}, response: {response.text}"
    json_data = response.json()
    assert json_data["status"] == "ok"

@allure.step("Validate response for existing user error")
def validate_existing_user_response(response):
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    json_data = response.json()
    assert json_data["status"] == "error"
    assert json_data["message"] == "User already exists"