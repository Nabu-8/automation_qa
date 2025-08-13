import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .signup_locators import Locators


class SignUpPage(BasePage):

    def __init__(self, driver, url="https://guest:welcome2qauto@qauto2.forstudy.space"):
        super().__init__(driver, url)
        self.locators = Locators

    @allure.step("Open Sign Up modal")
    def open_sign_up_modal(self):
        self.click(self.locators.sign_up_button_loc)

    @allure.step("Enter name: {name}")
    def enter_name(self, name):
        self.input_text(self.locators.name_input_loc, name)

    @allure.step("Enter last name: {last}")
    def enter_last_name(self, last):
        self.input_text(self.locators.last_name_input_loc, last)

    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        self.input_text(self.locators.email_input_loc, email)

    @allure.step("Enter password: {password}")
    def enter_password(self, password):
        self.input_text(self.locators.password_field_loc, password)

    @allure.step("Repeat password: {password}")
    def repeat_password(self, password):
        self.input_text(self.locators.repeat_password_field_loc, password)

    @allure.step("Fill sign-up form with provided data")
    def fill_form(self, name, last, email, password, repeat):
        self.enter_name(name)
        self.enter_last_name(last)
        self.enter_email(email)
        self.enter_password(password)
        self.repeat_password(repeat)

    @allure.step("Submit form")
    def submit_form(self):
        if self.is_register_button_enabled():
            self.click(self.locators.register_button_loc)
        else:
            print("Register button is disabled as expected — validation passed.")

    @allure.step("Check if register button is enabled")
    def is_register_button_enabled(self):
        el = self.wait.until(EC.presence_of_element_located(self.locators.register_button_loc))
        return el.is_enabled()

    def get_input_classes(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.get_attribute("class")

    def is_element_invisible(self, locator):
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False

    @allure.step("Get all visible error texts")
    def get_all_errors_text(self):
        errors = self._driver.find_elements(self.locators.field_error_feedback_loc)
        return " ".join([e.text for e in errors if e.is_displayed()])

    @allure.step("Check if registration was successful")
    def is_registration_successful(self):
        try:
            self.wait.until(EC.url_contains("/panel/garage"))
            return True
        except TimeoutException:
            return False

    @allure.step("Get alert text from modal")
    def get_alert_text(self):
        try:
            alert = self.wait.until(
                EC.visibility_of_element_located(self.locators.global_error_alert_loc)
            )
            return alert.text
        except TimeoutException:
            return ""

    @allure.step("Blur field: {locator}")
    def blur_field(self, locator=None):
        if locator is None:
            locator = self.locators.password_field_loc
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

        body = self._driver.find_element(By.TAG_NAME, "body")
        body.click()

    @allure.step("Blur and validate error message: {data}")
    def blur_field_and_wait_if_needed(self, data: dict, expected_error=None, timeout=5):
        if "last" in data:
            self.blur_field(self.locators.last_name_input_loc)
        elif "name" in data:
            self.blur_field(self.locators.name_input_loc)
            if expected_error:
                WebDriverWait(self._driver, timeout).until(
                    EC.text_to_be_present_in_element(
                        self.locators.error_text_loc,
                        expected_error
                    )
                )
        elif "email" in data:
            self.blur_field(self.locators.email_input_loc)
        elif "password" in data:
            self.blur_field(self.locators.password_field_loc)
        elif "repeat" in data:
            self.blur_field(self.locators.repeat_password_field_loc)