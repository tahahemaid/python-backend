import re

text = """
Contact us at taha.hameed@optimumpartners.co or call +966-5-345-5452.
You can also email taha.ahmed@gmail.com for help.
"""

email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
emails = re.findall(email_pattern, text)
print("Extracted Emails:", emails)

phone_pattern = r'\+?\d{1,3}[-\s]?\d{3}[-\s]?\d{3}[-\s]?\d{4}'
phones = re.findall(phone_pattern, text)
print("Extracted Phone Numbers:", phones)

def is_valid_email(email):
    return re.fullmatch(email_pattern, email) is not None

test_email = "tahahemaid@gmail.com"
print(f"Is '{test_email}' a valid email? ->", is_valid_email(test_email))
