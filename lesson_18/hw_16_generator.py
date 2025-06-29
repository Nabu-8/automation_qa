# Генератори:
#     Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_count_to_number_including_it(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    count = 0
    while count <= n:
        yield count
        count += 2

counter = even_count_to_number_including_it(10)

try:
    while True:
        print(next(counter))
except StopIteration:
    print("Completed")


# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator_to_n_including_it(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

fib = fibonacci_generator_to_n_including_it(13)

try:
    while True:
        print(next(fib))
except StopIteration:
    print("Completed")
