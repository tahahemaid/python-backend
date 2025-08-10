import re

def is_strong_password(password):
    
    if len(password) < 8:
        return False, "Too short (less than 8 characters)"
    if not re.search(r"[A-Z]", password):
        return False, "Missing uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Missing lowercase letter"
    if not re.search(r"\d", password):
        return False, "Missing digit"
    if not re.search(r"[!@#$%^&*]", password):
        return False, "Missing special character (!@#$%^&*)"
    return True, "Strong password"


def validate_passwords():
    try:
        with open("password", "r", encoding="utf-8") as infile, \
             open("strong_passwords.txt", "w", encoding="utf-8") as outfile, \
             open("password_errors.log", "w", encoding="utf-8") as error_log:

            for line_num, line in enumerate(infile, start=1):
                password = line.strip()
                if not password:
                    continue  

                is_valid, message = is_strong_password(password)
                if is_valid:
                    outfile.write(password + "\n")
                else:
                    error_log.write(f"Line {line_num}: '{password}' - {message}\n")

        print(" Password validation complete. Check 'strong_passwords.txt' and 'password_errors.log'.")

    except FileNotFoundError:
        print(" Error: 'password' file not found.")
    except OSError as e:
        print(f" File error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")


if __name__ == "__main__":
    validate_passwords()