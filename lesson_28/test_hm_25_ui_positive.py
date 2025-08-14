import pytest
import allure
from lesson_28.users_data import valid_data


@allure.epic("Sign Up Modal")
@allure.feature("UI Tests")
@pytest.mark.hw25()
class TestSignUpUIPositive:

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


    @allure.title("Modal window closes properly")
    @allure.story("Modal window closing")
    @pytest.mark.positive
    def test_is_modal_closed(self, sign_up_page):
        sign_up_page.open_sign_up_modal()
        sign_up_page.click(sign_up_page.locators.close_modal_icon_loc)
        assert sign_up_page.is_element_invisible(sign_up_page.locators.name_input_loc)