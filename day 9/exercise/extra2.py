def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' called {wrapper.call_count} time(s).")
        return func(*args, **kwargs)
    
    wrapper.call_count = 0  
    return wrapper


@call_counter
def greet(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet("Taha")
    greet("Fawaz")
    greet("Khalid")

    print(f"\nTotal calls to 'greet': {greet.call_count}")
