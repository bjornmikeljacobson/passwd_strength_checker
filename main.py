import re


def check_password_strength(passwd):
    # Check if password is at least 8 characters long
    if len(passwd) < 8:
        return "Weak"

    # Check if password contains at least one lowercase letter, one uppercase letter, and one digit
    if not re.search(r'[a-z]', passwd):
        return "Weak"
    if not re.search(r'[A-Z]', passwd):
        return "Weak"
    if not re.search(r'\d', passwd):
        return "Weak"

    # If password passes all checks, consider it strong
    return "Strong"


# Test the password checker
password = "Abc12345"
strength = check_password_strength(password)
print(f"Password {password} is {strength}")
