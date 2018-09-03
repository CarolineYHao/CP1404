from datetime import date

names_to_birthday = {"Jack": "12/4/1999", "Jill": "1/1/2000", "Harry": "27/3/1982"}
today = date.today()
for name, birthday in names_to_birthday.items():
    day, month, year = birthday.split("/")
    if int(month) >= today.month:
        if int(day) >= today.day:
            age = today.year - int(year)
    else:
        age = today.year - int(year) - 1

    print("{} is {}".format(name, age))