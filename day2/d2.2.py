def factorial(n):
   
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def get_user_input():
   
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Negative numbers are not allowed. Try again.")
                continue   
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")
            pass  


format_result = lambda n, f: "The factorial of {} is {}".format(n, f)


def main():

    number = get_user_input()

    print("Counting up to your number:")
    for i in range(1, number + 1):
        print(i, end=" ")
    print("\n")  

    result = factorial(number)

    print(format_result(number, result))


if __name__ == "__main__":
    main()