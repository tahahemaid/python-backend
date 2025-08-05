def second_largest(numbers: list) -> int:
    unique_numbers = list(set(numbers)) 
    if len(unique_numbers) < 2:
        raise ValueError("you have to put at least 2 unique numbers to the list.")

    unique_numbers.sort(reverse=True)  
    return unique_numbers[1]


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    return dict1 | dict2  


if __name__ == "__main__":
    
    numbers_list = [10, 5, 8, 20, 15, 20]
    print("The second-largest number is:", second_largest(numbers_list))

    dict_a = {"name": "Taha", "age": 23}
    dict_b = {"city": "New York", "age": 22} 
    merged_dict = merge_dictionaries(dict_a, dict_b)
    print("Merged dictionary:", merged_dict)

    dict_a |= dict_b
    print("In-place merged dictionary using |=:", dict_a)