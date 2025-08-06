from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url, timeout=10):
        self._driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self._driver.get(self.url)

    def input_text(self, locator, value):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value)

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def get_text(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text