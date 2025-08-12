from selenium.webdriver.common.by import By

class Locators:
    sign_up_button_loc = (By.CSS_SELECTOR, "button.hero-descriptor_btn.btn.btn-primary")
    name_input_loc = (By.ID, "signupName")
    last_name_input_loc = (By.ID, "signupLastName")
    email_input_loc = (By.ID, "signupEmail")
    password_field_loc = (By.ID, "signupPassword")
    repeat_password_field_loc = (By.ID, "signupRepeatPassword")
    register_button_loc = (By.CSS_SELECTOR, 'button.btn-primary[type="button"]')
    close_modal_icon_loc = (By.CSS_SELECTOR, 'button.close')
    error_text_loc = (By.XPATH, "//small[@class='text-danger']")
    field_error_feedback_loc = (By.CSS_SELECTOR, ".invalid-feedback")
    global_error_alert_loc = (By.CSS_SELECTOR, ".alert.alert-danger")
    registration_success_alert_loc = (By.CSS_SELECTOR, "app-alert-list")