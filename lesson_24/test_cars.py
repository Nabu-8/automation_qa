import pytest
import logging
from lesson_24.data_for_test import test_cases
from lesson_24.utils import validate_sorting

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log")
console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

@pytest.mark.hw21("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize("params", test_cases)
    def test_search(self, auth_session, params, total_cars_count):
        query_params = dict(params)
        if "sort_by" in query_params and query_params["sort_by"] == "":
            logger.warning(f"Empty 'sort_by' passed in params={query_params}")

        response, data = RequestHelper.send_request(auth_session, query_params)

        if params.get("sort_by") == "nonexistent_field":
            AssertionHelper.check_status_code(response, 400, query_params)
        else:
            AssertionHelper.check_status_code(response, 200, query_params)
            AssertionHelper.check_schema(data)
            AssertionHelper.limit_check(data, params.get('limit'), total_cars_count)

            sort_key = params.get('sort_by')
            if sort_key and data and sort_key in data[0]:
                validate_sorting(data, sort_key=sort_key)

class RequestHelper:

    @staticmethod
    def send_request(session, params):
        response = session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"GET cars with params={params}, response status code: {response.status_code}")
        try:
            data = response.json()
            logger.info(f"Response: {data}")
        except Exception as e:
            logger.warning(f"Error while JSON parse: {e}")
            data = None
        return response, data

class AssertionHelper:

    @staticmethod
    def check_status_code(response, expected_code, params):
        if response.status_code != expected_code:
            logger.warning(f"Expected status {expected_code} for params={params}, but got {response.status_code}")
        assert response.status_code == expected_code

    @staticmethod
    def check_schema(data):
        assert isinstance(data, list), "Should be list of results"

    @staticmethod
    def limit_check(data, limit, total_count):
        expected = min(limit, total_count) if limit is not None else total_count
        assert len(data) == expected, f"Expected {expected} records, got {len(data)}"