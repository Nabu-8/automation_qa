import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lesson_28.signup_locators import Locators
from lesson_28.users_data import valid_data, invalid_data, base_valid, random_email

@pytest.mark.hw25()
@pytest.mark.positive
@pytest.mark.parametrize("name, last, email, password, repeat", valid_data)
def test_valid_sign_up(sign_up_page, name, last, email, password, repeat):
    if len(last) > 21:
        pytest.skip(reason="JIRA-123: last name exceeds 21 characters")
    sign_up_page.open_sign_up_modal()
    sign_up_page.fill_form(name, last, email, password, repeat)
    sign_up_page.submit_form()
    assert sign_up_page.is_registration_successful()

@pytest.mark.hw25()
@pytest.mark.negative
def test_user_already_exists(sign_up_page, registered_user_email):
    sign_up_page.open_sign_up_modal()
    sign_up_page.enter_name("Test")
    sign_up_page.enter_last_name("User")
    sign_up_page.enter_email(registered_user_email)
    sign_up_page.enter_password("Pass1234")
    sign_up_page.repeat_password("Pass1234")
    sign_up_page.submit_form()

    alert = sign_up_page.get_alert_text()
    assert "User already exists" in alert

@pytest.mark.hw25()
@pytest.mark.negative
@pytest.mark.parametrize("data, expected_error", invalid_data)
def test_invalid_data_validation(sign_up_page, data, expected_error):
    all_data = {**base_valid, **data}
    if "email" not in all_data:
        all_data["email"] = random_email()

    if "last" in all_data and len(all_data["last"]) > 21:
        pytest.skip(reason="JIRA-123: last name exceeds 21 characters")

    sign_up_page.open_sign_up_modal()
    sign_up_page.fill_form(**all_data)

    if "last" in data:
        sign_up_page.blur_field(sign_up_page.locators.last_name_input_loc)
    elif "name" in data:
        sign_up_page.blur_field(sign_up_page.locators.name_input_loc)
        WebDriverWait(sign_up_page._driver, 5).until(EC.text_to_be_present_in_element(Locators.error_text_loc, expected_error))
    elif "email" in data:
        sign_up_page.blur_field(sign_up_page.locators.email_input_loc)
    elif "password" in data:
        sign_up_page.blur_field(sign_up_page.locators.password_field_loc)
    elif "repeat" in data:
        sign_up_page.blur_field(sign_up_page.locators.repeat_password_field_loc)

    if sign_up_page.is_register_button_enabled():
        sign_up_page.submit_form()
        errors = sign_up_page.get_all_errors_text()
        assert expected_error in errors
    else:
        print("Register button is disabled as expected — validation passed.")

@pytest.mark.hw25()
@pytest.mark.negative
@pytest.mark.parametrize("locator", [
    Locators.name_input_loc,
    Locators.last_name_input_loc,
    Locators.email_input_loc,
    Locators.password_field_loc,
    Locators.repeat_password_field_loc,
])
def test_invalid_input_class(sign_up_page, locator):
    sign_up_page.open_sign_up_modal()
    classes = sign_up_page.get_input_classes(locator)
    assert "ng-invalid" in classes

@pytest.mark.hw25()
@pytest.mark.positive
def test_is_modal_closed(sign_up_page):
    sign_up_page.open_sign_up_modal()
    sign_up_page.click(sign_up_page.locators.close_modal_icon_loc)
    assert sign_up_page.is_element_invisible(sign_up_page.locators.name_input_loc)