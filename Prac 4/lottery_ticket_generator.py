import random

NUMBERS = 45


def main():
    line_selection = int(input("How many quick picks?: "))
    for i in range(line_selection):
        line = create_line()
        print(sorted(line))


def create_line():
    line = []
    for i in range(6):
        number = random.randint(1, NUMBERS)
        while number in line:
            number = random.randint(1, NUMBERS)
        line.append(number)
    return line


main()
