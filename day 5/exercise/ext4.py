def merge_with_resolution(dict1: dict, dict2: dict) -> dict:
  
    merged = {}

    for key in dict1.keys() | dict2.keys():  
        if (v1 := dict1.get(key)) is not None and (v2 := dict2.get(key)) is not None:
            resolved_key = f"{key}_resolved"
            merged[resolved_key] = v1 + v2
        elif v1 is not None:
            merged[key] = v1
        else:
            merged[key] = dict2[key]

    return merged


if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}

    result = merge_with_resolution(dict1, dict2)
    print("Merged with conflict resolution:", result)