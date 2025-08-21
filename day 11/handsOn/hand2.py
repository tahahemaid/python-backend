from datetime import datetime


user_input = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")

try:

    dt = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

    print("Original format:", dt)
    print("Formatted date:", dt.strftime("%d-%m-%Y"))
    print("Formatted time:", dt.strftime("%I:%M %p"))  
    print("ISO format:", dt.isoformat())

except ValueError:
    print("Invalid format! Please enter date/time as YYYY-MM-DD HH:MM:SS")
