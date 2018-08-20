def main():
    min_length = int(input("Enter minimum length required: "))
    password = get_password(min_length)
    print("*" * len(password))


def get_password(min_length):
    password = input("Enter your password: ")
    while len(password) < min_length:
        print("Password needs to be at least {} characters.".format(min_length))
        password = input("Enter your password: ")
    return password


main()
