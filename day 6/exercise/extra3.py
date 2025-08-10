class InvalidLengthError(Exception):

    pass


class InvalidCharacterError(Exception):

    pass


def validate_username(username: str):
    
    if len(username) < 5 or len(username) > 15:
        raise InvalidLengthError("Username must be between 5 and 15 characters long.")
    if not username.isalnum():
        raise InvalidCharacterError("Username must contain only alphanumeric characters.")


def register_user():
    try:
        username = input("Enter a username: ").strip()
        validate_username(username)

        with open("users.txt", "a", encoding="utf-8") as file:
            file.write(username + "\n")

        print(f"Username '{username}' registered successfully!")

    except InvalidLengthError as e:
        print(f"Invalid Length: {e}")
    except InvalidCharacterError as e:
        print(f"Invalid Characters: {e}")
    except OSError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Registration attempt completed.")


if __name__ == "__main__":
    register_user()