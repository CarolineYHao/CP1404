TARIFF_TO_COST = {"11": 0.244618, "22": 0.34291, "31": 0.136928, "34": 0.19372, "15": 0.2832, "40": 0.271309}
key_list = (list(TARIFF_TO_COST.keys()))
current_tariff = (input("Enter your current tariff.\nChoose from{}: ".format(key_list)))
while current_tariff not in TARIFF_TO_COST:
    print("invalid tariff")
    current_tariff = (input("Enter your current tariff.\nChoose from{}: ".format(key_list)))
kWh_price = TARIFF_TO_COST[current_tariff]
kWh_use = float(input("Enter daily use in kWh: "))
billing_days = float(input("Enter number of billing days: "))
cost_cents = kWh_price * kWh_use * billing_days
cost_dollars = cost_cents / 100
print("Estimated bill: $" "{:.2f}".format(cost_dollars), )
