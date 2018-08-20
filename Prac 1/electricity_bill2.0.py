TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    kWh_price = choose_tariff()
    kWh_use = float(input("Enter daily use in kWh: "))
    billing_days = float(input("Enter number of billing days: "))
    cost_dollars = calculate_cost(kWh_price, kWh_use, billing_days)
    print("Estimated bill: $" "{:.2f}".format(cost_dollars), )


def choose_tariff():
    choice = (input("Enter current tariff(11 or 31): "))
    while choice != '11' or choice != '31':
        print("invalid tariff")
        choice = (input("Enter current tariff(11 or 31): "))
    if choice == '11':
        kWh_price = TARIFF_11
    else:
        kWh_price = TARIFF_31
    return kWh_price


def calculate_cost(kWh_price, kWh_use, billing_days):
    cost_cents = kWh_price * kWh_use * billing_days
    cost_dollars = cost_cents / 100
    return cost_dollars


main()
