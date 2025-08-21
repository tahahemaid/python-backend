import re
from datetime import datetime
import pytz

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.fullmatch(pattern, email) is not None

email = input("Enter your email address: ")
if is_valid_email(email):
    print("Valid email!")
else:
    print("Invalid email format.")
    exit()

print("\nHere are some common timezone names:")
print(" - UTC")
print(" - US/Eastern")
print(" - Europe/London")
print(" - Asia/Kolkata")
print(" - Australia/Sydney")
print(" - Asia/Amman")

timezone_name = input("Enter a timezone name from above (or any valid timezone): ")

try:
    timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(timezone)
    print(f"Current time in {timezone_name} is: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
except pytz.UnknownTimeZoneError:
    print("Invalid timezone name. Please try again with a valid timezone.")
