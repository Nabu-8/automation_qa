import json

def check_of_json(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            json.load(f)
        return f'{file} є валідним json файлом'
    except json.JSONDecodeError:
        return f'{file} не є валідним json файлом'
    except FileNotFoundError:
        return f'{file} не знайдено'

# Тест
print(check_of_json('localizations_en.json'))
print(check_of_json('localizations_ru.json'))
print(check_of_json('login.json'))
print(check_of_json('swagger.json'))
print(check_of_json('wrong_data.json'))
print(check_of_json('some_file_does_not_exist.json'))