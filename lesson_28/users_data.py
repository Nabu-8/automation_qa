import time
import random

def random_email():
    return f"autotest_{int(time.time())}_{random.randint(1000, 9999)}@test.com"

base_valid = {
    "name": "Test",
    "last": "User",
    "password": "Pass1234",
    "repeat": "Pass1234"
}

valid_data = [
    ("Test", "User", random_email(), "Pass1234", "Pass1234"),
    ("A" * 20, "B" * 20, random_email(), "Pass1234", "Pass1234"),  # граничні
]

invalid_data = [
    ({"name": "", "last": "User"}, "Name is invalid"),
    ({"name": "A", "last": "User"}, "Name is invalid"),
    ({"name": "A" * 22, "last": "User"}, "Name has to be from 2 to 20 characters long"),
    ({"name": "123", "last": "User"}, "Name is invalid"),
    ({"name": "$@!", "last": "User"}, "Name is invalid"),

    ({"name": "User", "last": ""}, "Last name is invalid"),
    ({"name": "User", "last": "A" * 22}, "Last name has to be from 2 to 20 characters long"),
    ({"name": "User", "last": "123"}, "Last name is invalid"),
    ({"name": "User", "last": "@@@"}, "Last name is invalid"),

    ({"email": "invalid"}, "Email is incorrect"),
    ({"email": "user.com"}, "Email is incorrect"),
    ({"email": ""}, "Email is incorrect"),

    ({"password": "short", "repeat": "short"}, "Password must be from 8 to 15"),
    ({"password": "password", "repeat": "password"}, "Password must contain at least"),
    ({"password": "PASSWORD", "repeat": "PASSWORD"}, "Password must contain at least"),
    ({"password": "Pass1234", "repeat": "WrongPass"}, "Passwords do not match"),
]