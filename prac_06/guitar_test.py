from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
second = Guitar("Second Guitar", 2012, 12.49)
print(gibson.get_age(), gibson.is_vintage())
print(second.get_age(), second.is_vintage())
