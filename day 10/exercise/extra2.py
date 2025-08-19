def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield sign * num
        sign *= -1

if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]

    for val in alternating_signs(nums):
        print(val)
