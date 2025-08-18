import tempfile
import pytest
import requests
from selenium import webdriver
from lesson_28.users_data import random_email
from lesson_28.sign_up_page import SignUpPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    temp_dir = tempfile.mkdtemp(prefix="chrome_profile_")
    options.add_argument(f"--user-data-dir={temp_dir}")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def sign_up_page(driver):
    page = SignUpPage(driver)
    page.open()
    return page

@pytest.fixture
def registered_user_email():
    email = random_email()
    url = "https://qauto2.forstudy.space/api/auth/signup"
    payload = {
        "name": "Test",
        "lastName": "User",
        "email": email,
        "password": "Pass1234",
        "repeatPassword": "Pass1234"
    }

    response = requests.post(url, json=payload)
    assert response.status_code in (200, 201), f"API signup failed: {response.text}"
    assert response.json()["status"] == "ok", f"API signup returned error: {response.json()}"

    return email