def create_student():
   
    student = {
        "name": "taha",
        "age": 23,
        "courses": ["Math", "Science", "History"]
    }
    print("Student Dictionary:")
    print(student)


def word_frequency(text: str) -> dict:
  
    words = text.split()
    return {word: words.count(word) for word in set(words)}


def squares_dict(n: int) -> dict:
   
    return {i: i ** 2 for i in range(1, n + 1)}


if __name__ == "__main__":
   
    create_student()

   
    text = "hello brautiful world "
    frequencies = word_frequency(text)
    print("\nWord Frequencies:")
    print(frequencies)

    squares = squares_dict(5)
    print("\nDictionary of Squares:")
    print(squares)