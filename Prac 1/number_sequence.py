def main():
    range_start = int(input("Enter start number"))
    range_end = int(input("Enter end number"))
    menu_choice = choose_option()
    while menu_choice != '4':
        if menu_choice == '1':
            range_start = change_for_even(range_start)
            print_sequence(range_start, range_end)
        elif menu_choice == '2':
            range_start = check_odd(range_start)
            print_sequence(range_start, range_end)
        elif menu_choice == '3':
            for i in range(range_start, range_end, 1):
                print(i ** 2)
        else:
            print("Invalid entry")
        range_start = int(input("Enter start number"))
        range_end = int(input("Enter end number"))
        menu_choice = choose_option()


def choose_option():
    print("(1)Show the even numbers from x to y\n"
          "(2)Show the odd numbers from x to y\n"
          "(3)Show the squares from x to y\n"
          "(4)Exit the program")
    menu_choice = input("Please choose from the menu: ")
    return menu_choice


def change_for_even(range_start):
    if range_start % 2 == 1:
        range_start = range_start + 1
    return range_start


def check_odd(range_start):
    if range_start % 2 == 0:
        range_start = range_start + 1
    return range_start


def print_sequence(range_start, range_end):
    for i in range(range_start, range_end, 2):
        print(i)


main()
