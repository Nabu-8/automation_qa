import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lesson_28.signup_locators import Locators
from lesson_28.users_data import valid_data, invalid_data, base_valid, random_email


@allure.epic("Sign Up Modal")
@allure.feature("UI Tests")
@pytest.mark.hw25()
class TestSignUpUI:

    @allure.title("Successful registration with valid data")
    @allure.story("Successful registration")
    @pytest.mark.positive
    @pytest.mark.parametrize("name, last, email, password, repeat", valid_data)
    def test_valid_sign_up(self, sign_up_page, name, last, email, password, repeat):
        if len(last) > 21:
            pytest.skip(reason="JIRA-123: last name exceeds 21 characters")

        sign_up_page.open_sign_up_modal()
        sign_up_page.fill_form(name, last, email, password, repeat)
        sign_up_page.submit_form()
        assert sign_up_page.is_registration_successful()

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

    @allure.title("Modal window closes properly")
    @allure.story("Modal window closing")
    @pytest.mark.positive
    def test_is_modal_closed(self, sign_up_page):
        sign_up_page.open_sign_up_modal()
        sign_up_page.click(sign_up_page.locators.close_modal_icon_loc)
        assert sign_up_page.is_element_invisible(sign_up_page.locators.name_input_loc)