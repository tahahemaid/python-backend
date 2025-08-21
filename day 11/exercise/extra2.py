import re

def extract_dates(text):
    
    pattern = r'\b(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})\b'
    matches = re.findall(pattern, text)
    
    dates = [f"{day}-{month}-{year}" for day, month, year in matches]
    return dates


user_text = input("Enter a text containing dates (DD-MM-YYYY or DD/MM/YYYY): ")

found_dates = extract_dates(user_text)

if found_dates:
    print("Found dates:")
    for date in found_dates:
        print(date)
else:
    print("No valid dates found.")
