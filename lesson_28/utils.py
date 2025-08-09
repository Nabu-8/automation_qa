def build_signup_payload(email):
    return {
        "name": "Test",
        "lastName": "User",
        "email": email,
        "password": "Pass1234",
        "repeatPassword": "Pass1234"
    }