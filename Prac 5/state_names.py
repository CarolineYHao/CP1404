"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

ABBREVIATION_TO_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                         "WA": "Western Australia",
                         "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state = input("Enter short state: ").upper()
while state != "":
    if state in ABBREVIATION_TO_NAMES:
        print(state, "is", ABBREVIATION_TO_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
for state, name in ABBREVIATION_TO_NAMES.items():
    print("{} is {}".format(state, name))
