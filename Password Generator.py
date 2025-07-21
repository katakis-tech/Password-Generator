import random
import string
import pyperclip


print("Welcome to the Password Generator!\n")


while True:
    # Ask the user how long the password should be
    try:
        length = int(input("How long should the password be? "))
    except ValueError:
        print("Please enter a number.")
        continue


    # Ask which character types to include
    use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Build character pool
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Safety check: Make sure at least one type was chosen
    if not characters:
        print("You need to select at least one character type! Try again.")
        exit()

    # Generate the password
    password = "".join(random.choice(characters) for i in range(length))

    # Show the password
    pyperclip.copy(password)
    print(f"\nYour new password is:\n{password}")
    print("Your password has been copied to the clipboard!")

    # Password strength logic
    strength = "Weak"

    if length >= 12 and sum([use_upper, use_lower, use_digits, use_symbols]) >= 3:
        strength = "Strong"
    elif length >= 8:
        strength = "Okay"

    print(f"Password Strength: {strength}")

    # If weak and they want to try again
    if strength == "Weak":
        retry = input("That password is weak. Would you like to try again? (y/n): ").lower()
        if retry == "y":
            print("\nLet's try again.\n")
            continue


    break