def merge_with_conflict_handling(dict1: dict, dict2: dict) -> dict:
    
    merged = dict1.copy()

    for key, value in dict2.items():
        if (existing := merged.get(key)) is not None:
            print(f"Conflict for key '{key}': dict1 has {existing}, dict2 has {value}")
        merged[key] = value  

    return merged


if __name__ == "__main__":
    dict1 = {"name": "Taha", "age": 23, "city": "Jeddah"}
    dict2 = {"age": 22, "country": "Saudi arabia", "city": "Al Zilfi"}

    result = merge_with_conflict_handling(dict1, dict2)
    print("\nMerged dictionary:", result)