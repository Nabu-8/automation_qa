import pytest
from lesson_10.hw9_pytest import *
from lesson_09.conftest import *


@pytest.mark.hw5
@pytest.mark.positive
def test_certain_user_added_to_0_people_records():
    people_records_copy_added_one = certain_user_added_to_0_people_records(people_records.copy(), new_user_add)
    assert people_records_copy_added_one[0] == new_user_add

@pytest.mark.hw5
@pytest.mark.positive
def test_swap_users():
    result = swap_users(people_records.copy(), index_swap_1, index_swap_2)
    assert result[index_swap_1] == people_records[index_swap_2]
    assert result[index_swap_2] == people_records[index_swap_1]

@pytest.mark.hw5
@pytest.mark.positive
def test_all_people_age_30_or_more_by_indexes():
    actual_result = all_people_age_30_or_more_by_indexes(people_records, indexes)
    expected_result = f'All people in modified list with records indexes {indexes} have age >=30'
    assert expected_result == actual_result

@pytest.mark.hw5
@pytest.mark.positive
def test_not_all_people_age_30_or_more_by_indexes():
    modified_records = certain_user_added_to_0_people_records(people_records.copy(), new_user_add)
    actual_result = all_people_age_30_or_more_by_indexes( modified_records, indexes)
    expected_result = f'Not all people in modified list with records indexes {indexes} have age >=30'
    assert expected_result == actual_result



@pytest.mark.hw8
@pytest.mark.positive
@pytest.mark.parametrize('expected_result, input_param', [
    ([10, 60, '"Не можу це зробити"'], array_with_value_error),  # 1 test
    ([0, -40, 20], array_without_exeption),  # 2 test
    (['"Не можу це зробити"', '"Не можу це зробити"', '"Не можу це зробити"'], array_without_values),  # 3 test
    (['"Не можу це зробити"', '"Не можу це зробити"', '"Не можу це зробити"'], array_with_wrong_values),  # 4 test
    ])
def test_sum_el_array(expected_result, input_param):
    actual_result = sum_el_array(input_param)
    assert actual_result == expected_result



@pytest.mark.hw7
@pytest.mark.positive
@pytest.mark.parametrize('str1, str2, expected_result', [
    ("Hello, world!", "world", 7),  # 1 test
    ("The quick brown fox jumps over the lazy dog", "cat", -1),  # 2 test
    ])
def test_find_substring(str1, str2, expected_result):
    actual_result = find_substring(str1, str2)
    assert actual_result == expected_result

