import unittest
from homeworks import *
from conftest import *


class TestHomeworkFiveFunctions(unittest.TestCase):

    def test_certain_user_added_to_0_people_records(self):
        people_records_copy_added_one = certain_user_added_to_0_people_records(people_records.copy(), new_user_add)
        self.assertEqual(people_records_copy_added_one[0], new_user_add)

    def test_swap_users(self):
        result = swap_users(people_records.copy(), index_swap_1, index_swap_2)
        self.assertEqual(result[index_swap_1], people_records[index_swap_2])
        self.assertEqual(result[index_swap_2], people_records[index_swap_1])

    def test_all_people_age_30_or_more_by_indexes(self):
        actual_result = all_people_age_30_or_more_by_indexes(people_records, indexes)
        expected_result = f'All people in modified list with records indexes {indexes} have age >=30'
        self.assertEqual(expected_result, actual_result)

    def test_not_all_people_age_30_or_more_by_indexes(self):
        modified_records = certain_user_added_to_0_people_records(people_records.copy(), new_user_add)
        actual_result = all_people_age_30_or_more_by_indexes( modified_records, indexes)
        expected_result = f'Not all people in modified list with records indexes {indexes} have age >=30'
        self.assertEqual(expected_result, actual_result)


class TestHomeworkightFunctions(unittest.TestCase):

    def test_sum_el_array_with_value_error(self):
        actual_result = sum_el_array(array_with_value_error)
        expected_result = [10, 60, '"Не можу це зробити"']
        self.assertEqual(expected_result, actual_result)

    def test_sum_el_array_without_exeption(self):
        actual_result = sum_el_array(array_without_exeption)
        expected_result = [0, -40, 20]
        self.assertEqual(expected_result, actual_result)

    def test_sum_el_array_without_values(self):
        actual_result = sum_el_array(array_without_values)
        expected_result = ['"Не можу це зробити"', '"Не можу це зробити"', '"Не можу це зробити"']
        self.assertEqual(expected_result, actual_result)

    def test_sum_el_array_with_wrong_values(self):
        actual_result = sum_el_array(array_with_wrong_values)
        expected_result = ['"Не можу це зробити"', '"Не можу це зробити"', '"Не можу це зробити"']
        self.assertEqual(expected_result, actual_result)


class TestHomeworkSevenFunctions(unittest.TestCase):

    def test_find_substring_is_in(self):
        actual_result = find_substring(str1_1, str1_2)
        expected_result = 7
        self.assertEqual(expected_result, actual_result)

    def test_find_substring_is_not_in(self):
        actual_result = find_substring(str2_1, str2_2)
        expected_result = -1
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__': # якщо цей файл запущено
    unittest.main(verbosity=2)