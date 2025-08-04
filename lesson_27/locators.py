from selenium.webdriver.common.by import By

class Locators:

    input_field_loc = (By.ID, "en")
    submit_button_loc = (By.ID, "np-number-input-desktop-btn-search-en")
    status_text_loc = (By.CSS_SELECTOR, "div.header__status-text")
    error_text_loc = (By.CSS_SELECTOR, "div.track__form-error span")
