def validate_positive_args(func):
    def wrapper(*args, **kwargs):

        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Invalid argument: {arg} (must be a number)")
            if arg <= 0:
                raise ValueError(f"Invalid argument: {arg} (must be positive)")


        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid argument '{key}': {value} (must be a number)")
            if value <= 0:
                raise ValueError(f"Invalid argument '{key}': {value} (must be positive)")

        return func(*args, **kwargs)
    return wrapper


@validate_positive_args
def divide(a, b):
    return a / b


if __name__ == "__main__":
    try:
        print(divide(10, 2))     
        print(divide(5, -3))     
    except ValueError as e:
        print("Error:", e)

    try:
        print(divide(a=8, b=0))  #
    except ValueError as e:
        print("Error:", e)

    try:
        print(divide("x", 4))    
    except ValueError as e:
        print("Error:", e)
