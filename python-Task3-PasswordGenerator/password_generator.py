# Project: Random Password Generator (OIBSIP - Python Programming Task 3)
# Author: Apeksha Suhas Phapale

import random
import string

def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    """Creates a pool of allowed characters based on user preferences."""
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool

def create_secure_password(length, pool):
    """Generates a random password of the requested length from the character pool."""
    return "".join(random.choice(pool) for _ in range(length))

def run_password_generator():
    print("\n" + "=" * 46)
    print("    PYTHON PASSWORD GENERATOR - APEKSHA       ")
    print("=" * 46)

    while True:
        # 1. Validate password length (minimum 8 characters enforced)
        try:
            length = int(input("\nEnter desired password length (minimum 8): "))
            if length < 8:
                print("Error: Password length must be at least 8 characters.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # 2. Choose character types (at least 2 types must be selected)
        print("\nSelect character types to include (y/n):")
        use_upper = input("Include Uppercase Letters (A-Z)? (y/n): ").strip().lower() == "y"
        use_lower = input("Include Lowercase Letters (a-z)? (y/n): ").strip().lower() == "y"
        use_digits = input("Include Numbers (0-9)? (y/n): ").strip().lower() == "y"
        use_symbols = input("Include Symbols (!@#$...)? (y/n): ").strip().lower() == "y"

        selected_count = sum([use_upper, use_lower, use_digits, use_symbols])
        if selected_count < 2:
            print("Error: Please select at least 2 character types for a strong password.")
            continue

        # 3. Generate and display the password
        pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols)
        password = create_secure_password(length, pool)

        print("\n-------------- GENERATED PASSWORD --------------")
        print(f"Your New Password : {password}")
        print("------------------------------------------------")

        # 4. Option to generate another password
        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for using Apeksha's Password Generator. Stay safe!")
            break

if __name__ == "__main__":
    run_password_generator()
