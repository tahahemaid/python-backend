from datetime import datetime

def calculate_exact_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")
        return

    today = datetime.today()


    years = today.year - birthdate.year


    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1


    months = today.month - birthdate.month
    if today.day < birthdate.day:
        months -= 1
    if months < 0:
        months += 12

    if today.day >= birthdate.day:
        days = today.day - birthdate.day
    else:
        last_month = today.month - 1 or 12
        year = today.year if today.month != 1 else today.year - 1
        last_day_prev_month = (datetime(year, last_month + 1, 1) - datetime(year, last_month, 1)).days
        days = last_day_prev_month - birthdate.day + today.day

    print(f"You are {years} years, {months} months, and {days} days old.")


user_input = input("Enter your birthdate (YYYY-MM-DD): ")
calculate_exact_age(user_input)
