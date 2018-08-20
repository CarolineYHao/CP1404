sales = float(input("Enter sales: $"))
while sales > 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Sales bonus amount is:", "{:.2f}".format(bonus))
    sales = float(input("Enter sales: $"))
