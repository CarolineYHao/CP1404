from prac_06.car import Car

MENU = "Menu: \nd) drive \nr) refuel \nq) quit \nEnter your choice: "
MENU_CHOICES = "drq"
INIT_FUEL = 100


def main():
    print("Lets Drive!")
    car_name = input("Enter your car name: ").title()
    car = Car(car_name, INIT_FUEL)
    menu_choice = validate_choice(car)
    while menu_choice != 'q':
        if menu_choice == 'd':
            drive_car(car)
        if menu_choice == 'r':
            refuel_car(car)
        menu_choice = validate_choice(car)
    print("Good bye {}'s driver".format(car_name))


def validate_choice(car):
    print(car)
    menu_choice = input(MENU).lower()
    while menu_choice not in MENU_CHOICES:
        print("Invalid Choice\n")
        menu_choice = input(MENU).lower()
    return menu_choice


def drive_car(car):
    drive_amount = int(input("How many km do you wish to drive?"))
    while drive_amount <= 0:
        print("Distance must be >= 0")
        drive_amount = int(input("How many km do you wish to drive?"))
    distance = car.drive(drive_amount)
    if car.fuel == 0:
        print("The car drove {}km and ran out of fuel.\n".format(distance))
    else:
        print("The car drove {}km.\n".format(distance))
    return


def refuel_car(car):
    fuel_amount = int(input("How many units of fuel do you want to add to the car? "))
    while fuel_amount <= 0:
        print("Fuel amount must be >= 0")
        fuel_amount = int(input("How many units of fuel do you want to add to the car? "))
    fuel = car.add_fuel(fuel_amount)
    print("Added {} units of fuel.\n".format(fuel))


main()
