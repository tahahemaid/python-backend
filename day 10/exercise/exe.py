def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

if __name__ == "__main__":
    try:
        count = int(input("Enter how many prime numbers you want: "))
        if count < 1:
            print("Please enter a number greater than 0.")
        else:
            prime_gen = generate_primes()
            print(f"\nFirst {count} prime numbers:")
            for _ in range(count):
                print(next(prime_gen))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
