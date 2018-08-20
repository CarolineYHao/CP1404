# for i in range(0, 101, 50):
#     print("{:3}".format(i))

import random

print(random.randint(5, 20))
# min 5, max 20
print(random.randrange(3, 10, 2))
# min 3, max 9, could not produce 4 as it goes in steps of 2
print(random.uniform(2.5, 5.5))
# random decimal numbers between 2.5 and 5.5
