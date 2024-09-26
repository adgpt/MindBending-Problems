# Password strength checker function
def check_password_strength(password):
    # Helper function to check common passwords
    def is_common_password(password):
        common_passwords = ["password", "123456", "qwerty", "abc123", "letmein"]
        return password in common_passwords

    # Initialize score
    score = 0

    # Check for length >= 8
    if len(password) >= 8:
        score += 1

    # Check for both lowercase and uppercase letters
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1

    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1

    # Check for special characters
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    if any(c in special_characters for c in password):
        score += 1

    # Check if it's not a common password
    if not is_common_password(password):
        score += 1

    # Classify strength based on score
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"


# Taking user input for the password
user_password = input("Enter your password: ")

# Getting the password strength
password_strength = check_password_strength(user_password)

# Output the result
print(f"Password strength: {password_strength}")
