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
        query = dict(params)
        if "sort_by" in query and query["sort_by"] == "":
            logger.warning(f"Empty 'sort_by' passed in params={query}")

        response = auth_session.get(f"{BASE_URL}/cars", params=query)

        logger.info(f"GET cars with params={query}, response status code: {response.status_code}")
        try:
            data = response.json()
            logger.info(f"Response: {data}")
        except Exception as e:
            logger.warning(f"Error while JSON parse: {e}")
            data = None

        if params.get("sort_by") == "nonexistent_field":
            if response.status_code != 400:
                logger.warning(f"Expected error for params={query} should be 400 but got {response.status_code}")
            assert response.status_code == 400, "Should be error code for wrong sort_by"
        else:
            assert response.status_code == 200, f"Response status code is {response.status_code} not 200"
            assert isinstance(data, list), "Should be list of results"

            limit = params.get('limit')

            if limit is not None:
                expected = min(limit, total_cars_count)
                assert len(data) == expected, f"Expected {expected} records, got {len(data)}"
            else:
                assert len(data) == total_cars_count, f"Expected all {total_cars_count} records by default, got {len(data)}"

            sort_key = params.get('sort_by')
            if sort_key and data and sort_key in data[0]:
                validate_sorting(data, sort_key=sort_key)