import random

NUMBERS_START = 1
NUMBERS_END = 45


def main():
    line_selection = int(input("How many quick picks?: "))
    for i in range(line_selection):
        line = create_line()
        print(sorted(line))


def create_line():
    line = []
    for i in range(6):
        number = random.randint(NUMBERS_START, NUMBERS_END)
        while number in line:
            number = random.randint(NUMBERS_START, NUMBERS_END)
        line.append(number)
    return line


main()
