LOWER = 33
UPPER = 127
MIN_COLUMN = 1
MAX_COLUMN = 10
NUMBER_OF_VALUES = UPPER - LOWER + 1


def main():
    number = get_number()
    print("The character for {} is {}".format(number, chr(number)))
    character_input = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character_input, ord(character_input)))
    columns = int(input("Enter the number of columns you'd like (1-10): "))
    print_by_columns(columns)


def get_number():
    try:
        number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
        while number > LOWER or number > UPPER:
            print("Please enter a valid number!")
            number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
            pass
    except ValueError:
        print("Please enter a valid number!")
    return number


# def print_ascii_table():
#     for i in range(LOWER, UPPER+1):
#         character = chr(i)
#         if i == 127:
#             character = "delete"
#         print("{:3} {}".format(i, character))


def print_by_columns(columns):
    value = LOWER
    while columns < 1 or columns > 10:
        print("Please input a column number between 1 and 10: ")
        columns = int(input("Enter the number of columns you'd like (1-10): "))
    rows = NUMBER_OF_VALUES // columns
    for row in range(rows):
        for column in range(columns):
            print("{:6} {:>2}".format(value, chr(value)), end="")
            value += 1
        print()
    starting_value = value
    for value in range(starting_value, UPPER + 1):
        print("{:6} {:>2}".format(value, chr(value)), end="")


main()
