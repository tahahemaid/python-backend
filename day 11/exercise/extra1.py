import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return re.fullmatch(pattern, email) is not None

email = input("Enter an email address to validate: ")

if validate_email(email):
    print("Valid email address!")
else:
    print("Invalid email address!")
