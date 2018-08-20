subtotal = 0
items = int(input('Enter number of items: '))
while items < 0:
    print("Invalid number of items!")
    items = int(input('Enter number of items: '))
for i in range(1, items + 1):
    item_price = float(input("Price of item number " + str(i) + ": "))
    subtotal = subtotal + item_price
if subtotal > 100:
    total_price = subtotal * 0.9
else:
    total_price = subtotal
print("Total price for", items, "items is $", "{:.2f}".format(total_price))
