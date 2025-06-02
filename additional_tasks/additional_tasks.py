# 1 - Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist.
# В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)
australia_blacklist = {'Alina', 'Leo', 'Nick', 'Maggie', 'Eric'}
poker_blacklist = {'Marta', 'Leo', 'Keanu', 'Maggie'}
alcohol_blacklist = {'Maggie', 'John', 'Leon', 'Amy', 'Leo'}
if australia_blacklist & poker_blacklist & alcohol_blacklist:
    for name in australia_blacklist & poker_blacklist & alcohol_blacklist:
        print(f'The winner is {name}!')
else:
    print(f'This time there is no winner!')

# 2 - Словник має наступні дані: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}
# Використвоючі f-string вивести: "User_name is living in place_name" для кожного юзера. Використовувати цикл
dictionary = {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}
for key, value in dictionary.items():
    print(f'{key} is living in {value}')

# 3 - Порахувати та вивести(print) кількість букв в строці.
# Юзер щось вводить(input)
# Ваша задача надрукувати кількість кожного символу того що він ввів.
# Прикдад:
# Юзер вводить:
# My name is Emmy Santiago.
# ВИ прінтаете щось накшталт:
# M = 1, y = 2, n = 2, ...(або в іншому форматі, це не принциповоб головне, що б чітко було зрозуміло скільки разів
# зустрічаеться кожна буква)
# Тобто кожну букву та скільки разів вона зустрічаеться
user_input = 'My name is Emmy Santiago'
dict = {}
for letter in user_input:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1
print(dict)

# 4
# Вирішити задачу 3 без словника за 2 строки:
# 1 строка це input
# 2 строка це рішення
user_input = 'My name is Emmy Santiago'
print({user_input: sum(1 for letter in user_input if letter == user_input) for user_input in set(user_input)})

# 5 - це ми не прозодили на лекції, але в матеріалах по циклаї є рішення:
# Ви створюєте список в якому може бути None(а може і не бути)
# Мета: надрукувати "There is no None" у випадку якщо None не зустрічаеться у списку

list = [2, 5, 10, None, 15, 8, 5, 11]
for item in list:
    if item is None:
        break
else:
     print("There is no None")


# Умови:
# По списку ми йдемо циклом
# Не створювати змінні(крім списку про який сказано вище)
# використати if 1 раз
# Не використовувати методи/функції/класи