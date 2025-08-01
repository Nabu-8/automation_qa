from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import Locators

class NovaPoshtaTrackingPage(BasePage):

    def __init__(self, driver, url="https://tracking.novaposhta.ua/#/uk"):
        super().__init__(driver, url)
        self.locators = Locators

    def enter_tracking_number(self, ttn):
        self.input_text(self.locators.input_field_loc, ttn)
        self.click(self.locators.submit_button_loc)

    def get_status_text(self):
        try:
            return self.get_text(self.locators.status_text_loc)
        except TimeoutException:
            try:
                return self.get_text(self.locators.error_text_loc)
            except TimeoutException:
                return "Status is not found"