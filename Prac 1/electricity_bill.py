kWh_price = float(input("Enter cents per kWh: "))
kWh_use = float(input("Enter daily use in kWh: "))
billing_days = float(input("Enter number of billing days: "))
cost_cents = kWh_price * kWh_use * billing_days
cost_dollars = cost_cents / 100
print("Estimated bill: $" "{:.2f}".format(cost_dollars))
