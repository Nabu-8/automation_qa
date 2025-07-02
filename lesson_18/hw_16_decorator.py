# Декоратори:
#     Напишіть декоратор, який логує аргументи та результати викликаної функції.
import logging

logging.basicConfig(
    filename='login_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def log_event(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            args_str = ", ".join(str(arg) for arg in args)
            kwargs_str = ", ".join(f"{key}={value}" for key, value in kwargs.items())
            all_args = ", ".join(filter(None, [args_str, kwargs_str])) or "no args"
            logging.info(f"Function: {func.__name__}; all args: {all_args}; result: {result}")
            return result
        except Exception as e:
            logging.error(f"{func.__name__} failed with args={args}, kwargs={kwargs}, error={e}")
            raise

    return wrapper

@log_event
def say_hello():
    return "Hello!"

@log_event
def greeting_to(name):
    return f"Hello, {name}!"

@log_event
def users_city(name, city, age):
    return  f"{name} is {age} y.o. and she lives in {city}!"

@log_event
def send_message(to, text):
    return f"{to}! {text}"

print(say_hello())
print(users_city("Cathy", "Toronto", 20))
print(greeting_to("Cathy"))
print(send_message("Cathy", text="How are you doing?"))


#     Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def skip_errors(fn):
    def wrapper(*args, **kwargs):
        try:
           return fn(*args, **kwargs)
        except Exception as e:
            print(f"Can't run {fn.__name__} because of: {e}")
            return 'Error'

    return wrapper


@skip_errors
def division(num1, num2):
    return num1 / num2

@skip_errors
def get_element(lst, index):
    return lst[index]

@skip_errors
def get_value(d, key):
    return d[key]

@skip_errors
def to_int(s):
    return int(s)

print(division(10,2))
print(division(1,0))
print(get_element([1, 2, 3], 10))
print(get_value({"a": 1}, "b"))
print(to_int("abc"))