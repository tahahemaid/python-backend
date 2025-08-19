vowels = {'a', 'e', 'i', 'o', 'u'}

user_input = input("Enter a word: ")

result = {char.upper() for char in user_input.lower() if char in vowels}

print("Vowels found are writen as an uppercase :", result)
