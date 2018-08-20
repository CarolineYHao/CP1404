'''Using a population of 1000 gophers, population is simulated for the next 10 years by using random values
 between 10% - 20% for population increase and  between 5% - 25% population decrease each year'''

import random

INITIAL = 1000
YEARS = 10
GREETING = "Welcome to the Gopher Population Simulator!\nStarting population: {}\nYear 1".format(INITIAL)


def main():
    print(GREETING)
    gophers = INITIAL
    for i in range(2, YEARS + 1):
        gophers_born = increase_gophers(gophers)
        gophers_died = decrease_gophers(gophers)
        print()
        print("{} gophers were born, {} gophers died".format(gophers_born, gophers_died))
        gophers = gophers + gophers_born - gophers_died
        print("Population: {}".format(gophers))
        print("Year {}".format(i))


def increase_gophers(gophers):
    gophers_born = int(gophers * random.uniform(0.1, 0.2))
    return gophers_born


def decrease_gophers(gophers):
    gophers_died = int(gophers * random.uniform(0.05, 0.25))
    return gophers_died


main()
