import re

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    max_value = 25
    # Complete the while loop condition.
    while number * multiplier <= max_value:
        print(f'{number}x{multiplier}={number * multiplier}')
        multiplier += 1
        # Enter the action to take if the result is greater than 25
        # Increment the appropriate variable

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_two(a, b):
    added = a + b
    return added

print(f'Сума чисел дорівнює {add_two(3, 5)}.')

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_average(list):
    return sum(list)/(len(list))

list = [2, 5, 10, 15, 8, 5, 11]
average = arithmetic_average(list)
print(f'Середнє арифметичне списку чисел {list} дорівнює {average}.')

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string):
    return string[::-1]

string = 'Hello world!'
print(reverse_string(string))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def list_longest_word(words):
    return max(words, key=len)

words = ["apple", "banana", "cherry", "dog", "elephant", "flower", "guitar", "house", "island", "jungle"]
print(f'Найдовше слово у списку {words} це {list_longest_word(words)}.')

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 7 == ##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
def paragraph_end_to_space(text):
    text = text.replace("\n", " ")
    return text

print(paragraph_end_to_space(adwentures_of_tom_sawer))

# task 8
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
def text_title_words(text):
    count = 0
    for word in text.split():
        if word.istitle():
            count = count + 1
    return count

print(f'У тексті {text_title_words(adwentures_of_tom_sawer)} слів починається з Великої літери.')

# task 9
""" Перевірте чи починається якесь речення з "By the time".
"""
def search_in_text(search_for, text):
    text_sentences = re.split(r'(?<=[.!?])\s+', text)
    if any(sentence.startswith(search_for) for sentence in text_sentences):
        answer = 'В тексті є речення яке починаються з "By the time"'
    else:
        answer = 'В тексті немає реченнь які починається з "By the time".'
    return answer

print(search_in_text("By the time", adwentures_of_tom_sawer))

# task 10
#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
def input_unique_symbols(user_input):
    return len(set(user_input)) > 10

line = input('Внесіть символи: ')
print(input_unique_symbols(line))