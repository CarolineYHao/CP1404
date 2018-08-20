LOWER = 33
UPPER = 127
MIN_COLUMN = 1
MAX_COLUMN = 10
NUMBER_OF_VALUES = UPPER - LOWER + 1


def main():
    convert_from_character()
    convert_from_number()
    columns = int(input("Enter the number of columns you'd like (1-10): "))
    print_by_columns(columns)


def convert_from_character():
    character_input = input("Enter a character: ")
    ascii_code = ord(character_input)
    print("The ASCII code for {} is {}".format(character_input, ascii_code))


def convert_from_number():
    number_input = int(input("Enter a number between 33 and 127: "))
    while (number_input < 33) or (number_input > 127):
        print("Invalid number!")
        number_input = int(input("Enter a number between 33 and 127: "))
        character_output = chr(number_input)
        if number_input == 127:
            character_output = "delete"
        print("The character for {} is {}".format(number_input, character_output))


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
