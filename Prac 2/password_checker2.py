MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    if (MIN_LENGTH < len(password)) and (len(password) < MAX_LENGTH):
        for char in password:
            count_lower += count_lower_char(char)
            count_upper += count_upper_char(char)
            count_digit += count_digit_char(char)
            count_special += count_special_char(char)
            print(count_lower, count_upper, count_digit, count_special)
            pass
        if (count_lower, count_upper or count_digit) == 0:
            return False
        if SPECIAL_CHARS_REQUIRED:
            if count_special == 0:
                return False
            else:
                return True
        else:
            return True
    else:
        return False


def count_lower_char(char):
    if char.islower():
        return 1
    else:
        return 0


def count_upper_char(char):
    if char.isupper():
        return 1
    else:
        return 0


def count_digit_char(char):
    if char.isdigit():
        return 1
    else:
        return 0


def count_special_char(char):
    if char in SPECIAL_CHARACTERS:
        return 1
    else:
        return 0


main()
