import pytest
from .nova_poshta_page import NovaPoshtaTrackingPage

@pytest.mark.hw24()
@pytest.mark.parametrize("ttn, expected_status", [
    ("20400467719169", "Отримана"),
    ("11111111111", "Видалено"),
    ("50505050505", "Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців,"
                    " будь ласка, зверніться у контакт-центр: "),
])
def test_tracking_status(driver, ttn, expected_status):
    page = NovaPoshtaTrackingPage(driver)
    page.open()
    page.enter_tracking_number(ttn)
    actual_status = page.get_status_text()
    assert expected_status in actual_status, \
        f"Expected: {expected_status}, actual: {actual_status}"