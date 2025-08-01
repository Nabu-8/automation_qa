import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from lesson_26.frames_data import frames_data


@pytest.mark.hw23()
@pytest.mark.parametrize("frame", frames_data)
def test_frame(driver, frame):
    driver.get("http://localhost:8000/dz.html")

    driver.switch_to.frame(driver.find_element(By.ID, frame["frame_id"]))

    input_field = driver.find_element(By.ID, frame["input_id"])
    input_field.send_keys(frame["secret_phrase"])
    driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()    # ОК to close alert

    input_field.clear()
    input_field.send_keys("Some wrong text!")
    driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "Введено неправильний текст!"
    alert.accept()

    driver.switch_to.default_content()