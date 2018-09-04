"""
Looks up hexadecimal colour codes
"""

HEX_TO_COLOUR = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "beige": "#f5f5dc",
                 "black": "#000000", "burlywood": "#deb887", "cadetblue": "#5f9ea0", "coral": "#ff7f50",
                 "darkviolet": "#9400d3:", "gray": "#bebebe"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in HEX_TO_COLOUR:
        print(colour_name, "is", HEX_TO_COLOUR[colour_name])
    else:
        print("Invalid colour name")
    state = input("Enter colour name: ").lower()
