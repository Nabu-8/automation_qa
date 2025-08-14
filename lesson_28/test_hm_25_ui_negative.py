import pytest
import allure
from lesson_28.signup_locators import Locators
from lesson_28.users_data import invalid_data, base_valid, random_email


@allure.epic("Sign Up Modal")
@allure.feature("UI Tests")
@pytest.mark.hw25()
class TestSignUpUINegative:

    @allure.title("Registration attempt with already existing user")
    @allure.story("Registration with existing user")
    @pytest.mark.negative
    def test_user_already_exists(self, sign_up_page, registered_user_email):
        sign_up_page.open_sign_up_modal()
        sign_up_page.fill_form("Test", "User", registered_user_email, "Pass1234", "Pass1234")
        sign_up_page.submit_form()

        alert = sign_up_page.get_alert_text()
        assert "User already exists" in alert

    @allure.title("Registration with invalid form data")
    @allure.story("Invalid registration")
    @pytest.mark.negative
    @pytest.mark.parametrize("data, expected_error", invalid_data)
    def test_invalid_data_validation(self, sign_up_page, data, expected_error):
        all_data = {**base_valid, **data}
        if "email" not in all_data:
            all_data["email"] = random_email()

        if "last" in all_data and len(all_data["last"]) > 21:
            pytest.skip(reason="JIRA-123: last name exceeds 21 characters")

        sign_up_page.open_sign_up_modal()
        sign_up_page.fill_form(**all_data)

        sign_up_page.blur_field_and_wait_if_needed(data, expected_error)

        if sign_up_page.is_register_button_enabled():
            sign_up_page.submit_form()
            errors = sign_up_page.get_all_errors_text()
            assert expected_error in errors
        else:
            print("Register button is disabled as expected — validation passed.")

    @allure.title("Visual check of invalid input field class")
    @allure.story("Invalid input class check")
    @pytest.mark.negative
    @pytest.mark.parametrize("locator", [
        Locators.name_input_loc,
        Locators.last_name_input_loc,
        Locators.email_input_loc,
        Locators.password_field_loc,
        Locators.repeat_password_field_loc,
    ])
    def test_invalid_input_class(self, sign_up_page, locator):
        sign_up_page.open_sign_up_modal()
        classes = sign_up_page.get_input_classes(locator)
        assert "ng-invalid" in classes