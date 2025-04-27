# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers = [5, 12, 7, 3, 19, 1, 8, 15]
even_numbers = [number for number in numbers if number % 2 == 0]
print(f'У списку {numbers} є такі {even_numbers} парні числа, а їх сума дорівнює {sum(even_numbers)}.')