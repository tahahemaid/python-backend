def remove_duplicates(input_list: list) -> list:
    """
    Remove duplicates from a list using a set.

    Args:
        input_list (list): A list with possible duplicates.

    Returns:
        list: A list of unique values.
    """
    return list(set(input_list))


def set_operations(A: set, B: set) -> dict:
    """
    Perform union, intersection, difference, and symmetric difference on two sets.

    Args:
        A (set): First set.
        B (set): Second set.

    Returns:
        dict: Dictionary with results of each operation.
    """
    return {
        "union": A | B,
        "intersection": A & B,
        "difference (A - B)": A - B,
        "symmetric_difference": A ^ B
    }


def count_unique_words(text: str) -> int:
    
    words = text.split()
    unique_words = set(words)
    return len(unique_words)


if __name__ == "__main__":
    input_list = [3, 5, 7, 5, 9, 3]
    unique_list = remove_duplicates(input_list)
    print("Unique nums from list:", unique_list)


    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    results = set_operations(A, B)
    print("\nSet Operations:")
    for operation, result in results.items():
        print(f"{operation}: {result}")


    sentence = "mercedes bmw gmc bmw mercedes gmc toyota toyota"
    unique_word_count = count_unique_words(sentence)
    print(f"\nNumber of unique words in sentence: {unique_word_count}")