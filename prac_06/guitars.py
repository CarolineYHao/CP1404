from prac_06.guitar import Guitar

guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Name: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print("{} ({}) : ${.2f} added".format(name, year, cost))
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars):
    vintage_string = " vintage" if Guitar.is_vintage(guitar) else ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                              vintage_string))
    print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{3}".format(i + 1, guitar, vintage_string))
