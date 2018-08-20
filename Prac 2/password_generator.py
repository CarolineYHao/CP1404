import random

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
SPECIAL = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    password_length = int(input("Enter password length required: "))
    capital_needed = input("Is a capital letter required?(Y/N): ").upper()
    numbers_needed = input("Are numbers required?(Y/N): ").upper()
    special_needed = input("Are special characters required?(Y/N): ").upper()
    password = generate_password(password_length, capital_needed, numbers_needed, special_needed)
    print("Your generated password is: {}".format(password))


def generate_password(password_length, capital_needed, numbers_needed, special_needed):
    password = ""
    for i in range(password_length):
        character_choice = random.randint(1, 3)
        if character_choice == 1:
            if capital_needed == 'Y':
                password += random.choice(ALPHABET.upper())
            else:
                password += random.choice(ALPHABET)
        elif character_choice == 2:
            if numbers_needed == 'Y':
                password += random.choice(NUMBERS)
            else:
                password += random.choice(ALPHABET)
        else:
            if special_needed == 'Y':
                password += random.choice(SPECIAL)
            else:
                password += random.choice(ALPHABET)
    return password


main()
