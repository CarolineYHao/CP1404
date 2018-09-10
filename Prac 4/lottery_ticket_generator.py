import random

LINE_LENGTH = 6

NUMBERS_START = 1
NUMBERS_END = 45


def main():
    line_selection = int(input("How many quick picks?: "))
    for i in range(line_selection):
        number_line = create_line()
        print(sorted(line))


def create_line():
    number_line = []
    for i in range(LINE_LENGTH):
        number = random.randint(NUMBERS_START, NUMBERS_END)
        while number in line:
            number = random.randint(NUMBERS_START, NUMBERS_END)
        line.append(number)
    return line


main()
