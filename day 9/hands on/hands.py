def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_function_call
def add(x, y):
    return x + y

@log_function_call
def greet(name, age=20):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(add(5, 7))
    print(greet("Taha", age=30))
