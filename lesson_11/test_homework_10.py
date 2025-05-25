import os
import pytest
from lesson_11.homework_10 import log_event

LOG_FILE = 'login_system.log'

@pytest.mark.hw10
@pytest.mark.positive
@pytest.mark.parametrize('username, status', [
    ("Katy", "success"),
    ("Nick", "expired"),
    ("Rita", ""),
])
def test_log_event_writes_to_file(username, status):
    log_event(username, status)
    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        log_contents = file.read()
    expected_text = f"Login event - Username: {username}, Status: {status}"
    assert expected_text in log_contents