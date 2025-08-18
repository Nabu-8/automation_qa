import pytest
import allure
from lesson_28.users_data import random_email
from lesson_28.api_helpers import (
    send_signup_request,
    validate_successful_response,
    validate_existing_user_response
)

@allure.suite("HW25 API Tests")
@allure.epic("Sign Up Modal")
@allure.feature("API Tests")
@pytest.mark.hw25()
@pytest.mark.api_test
class TestSignUpAPI:

    @allure.title("Successful user registration via API")
    @allure.story("Successful registration")
    @pytest.mark.positive
    def test_successful_registration_api(self):
        email = random_email()
        response = send_signup_request(email)
        validate_successful_response(response)

    @allure.title("Registration attempt with already registered email")
    @allure.story("Registration with existing user")
    @pytest.mark.negative
    def test_user_already_exists_api(self, registered_user_email):
        response = send_signup_request(registered_user_email)
        validate_existing_user_response(response)

# ri allure-results -r -fo
# pytest -m hw25 --alluredir=allure-results
# allure serve allure-results
