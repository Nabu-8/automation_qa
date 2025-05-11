# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

def sum_el_array(array):
    summ_numbers = []
    for string in array:
        string_parts = string.split(',')
        try:
            res = sum([int(part) for part in string_parts])
        except ValueError:
            res = '"Не можу це зробити"'
        finally:
            summ_numbers.append(res)
    return summ_numbers

array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
result = sum_el_array(array)
print(*result, sep=', ')