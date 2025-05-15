import unittest
from homeworks import *


# Data for tests 1-4 (HM 5.2)
# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
new_user_add = 'Rita', 'New', 30, 'Software Engineer', 'Jacksonville'
index_swap_1 = 1
index_swap_2 = 5
indexes = [6, 10, 13]


# Data for test 5-8 (HM 8)
# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

array_with_value_error = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
array_without_exeption = ["0,0,0,0", "1,2,3,4,-50", "5,9,1,2,3"]
array_without_values = [None, "", " "]
array_with_wrong_values = ["12.5,1,2,3,4", "1,2,?,4", [1, 2, 3]]


# Data for test 9-10 (HM 7)
# Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка."""
str1_1 = "Hello, world!"
str1_2 = "world"

str2_1 = "The quick brown fox jumps over the lazy dog"
str2_2 = "cat"




class TestHomeworkFunctions(unittest.TestCase):

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