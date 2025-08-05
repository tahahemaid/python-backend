def manipulate_data(numbers: list) -> dict:
    
    sorted_nums = sorted(numbers)

    
    filtered_nums = [num for num in numbers if num % 2 != 0]

    squared_nums = [num ** 2 for num in numbers]

    return {
        
        "filtered": filtered_nums,
        "sorted": sorted_nums,
        "transformed": squared_nums
    }


def manipulate_tuples(data: tuple) -> dict:
    sortedTuple = tuple(sorted(data))
    filteredTuple = tuple(num for num in data if num % 2 != 0)
    squaredTuple = tuple(num ** 2 for num in data)

    return {
        "filtered": filteredTuple,
        "sorted": sortedTuple,
        "transformed": squaredTuple
    }


if __name__ == "__main__":
    num_list = [10, 3, 5, 8, 1, 4]
    num_tuple = (7, 2, 9, 5, 6)

    print("List manipulated results:")
    print(manipulate_data(num_list))

    print("\nTuple manipulated results:")
    print(manipulate_tuples(num_tuple))


    