def count_word_frequency(file_path: str) -> dict:
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        import string
        translator = str.maketrans("", "", string.punctuation)
        text = text.translate(translator).lower()

        words = text.split()

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        return word_count

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    filename = "sample.txt"  

    result = count_word_frequency(filename)
    if result:
        print("Word Frequency Count:")
        for word, freq in sorted(result.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {freq}")