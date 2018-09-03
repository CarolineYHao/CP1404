"""
Write a function that takes two parallel lists as input parameters and returns a dictionary where keys are from the
first list and the values are from the second. Use the above example as a test case.
"""

names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
names_to_birthday = {}
for i, name in enumerate(names):
    names_to_birthday[name] = dates_of_birth[i]
print(names_to_birthday)