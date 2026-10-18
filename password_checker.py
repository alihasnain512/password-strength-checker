import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!, @, #, etc.).")

    return score, feedback

def main():
    print("--- Password Strength Checker ---")
    user_password = input("Enter a password to evaluate: ")
    score, feedback = check_password_strength(user_password)

    print(f"\nPassword Score: {score}/5")
    if score == 5:
        print("Strength: Strong! Your password meets all security criteria.")
    elif score >= 3:
        print("Strength: Moderate. Consider improving it.")
    else:
        print("Strength: Weak. Follow the recommendations below:")

    for item in feedback:
        print(f" - {item}")

if __name__ == "__main__":
    main()