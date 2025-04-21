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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Task 1")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""
print("Task 2")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("Task 3")
import re
adwentures_list = re.split(r'\s+', adwentures_of_tom_sawer)
adwentures_of_tom_sawer = ' '.join(adwentures_list)
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Task 4")
search_for = 'h'
amount = adwentures_of_tom_sawer.count(search_for)
print(f'У тексті літера "{search_for}" зустрічається {amount} разів.')


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("Task 5")
count = 0
for word in adwentures_of_tom_sawer.split():
    if word.istitle():
        count = count + 1
print(f'У тексті {count} слів починається з Великої літери.')


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("Task 6")
search_word = 'Tom'
if adwentures_of_tom_sawer.find(search_word) != -1:
    first_index = adwentures_of_tom_sawer.find(search_word)
    print(f'The word "{search_word}" occurs for the second time on {adwentures_of_tom_sawer.find(search_word, first_index + 1)} position.')
else:
    print(f'Word "{search_word}" is not found in the text.')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("Task 7")
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 8")
print(adwentures_of_tom_sawer_sentences[3])
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("Task 9")
if any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences):
    print('В тексті є речення яке починаються з "By the time"')
else:
    print('В тексті немає реченнь які починається з "By the time".')


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("Task 10")
print(f'В останньому реченні {len(adwentures_of_tom_sawer_sentences[-1].split())} слів.')