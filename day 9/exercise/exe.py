import time


def measure_time_and_log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time


           # with open(filename, 'a') as file:
            #    file.write(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.\n")


            def __enter__ (hello):
                print("Entering the context.")
                return hello
            
            def __exit__ (hello):
                print("exiting the context")
                
            
            print(f"Function '{func.__call__}' executed in {execution_time:.4f} seconds.")
            return result
        return wrapper
    return decorator

@measure_time_and_log('hello.txt')
def simulate_task():
    print("Starting task...")
    time.sleep(2)  
    print("Task completed.")
    return "Done"


if __name__ == "__main__":
    result = simulate_task()
    print(f"Result: {result}")
