words = ['cat', 'dog', 'bird']

result = {word: {char: ord(char) for char in word} for word in words}

print(result)
