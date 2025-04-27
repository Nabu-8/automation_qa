#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
line = input('Внесіть символи: ')
if len(set(line)) > 10:
    print('True')
else:
    print('False')

# print(set(line))