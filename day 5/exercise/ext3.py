def get_valid_input():
   
    while (num := int(input("Enter a number greater than 10: "))) <= 10:
        print("That's not greater than 10. Try again.")
    print(f"Valid input received: {num}")


if __name__ == "__main__":
    get_valid_input()