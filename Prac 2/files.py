out_file = open("name.txt", 'w')
name = input("Enter your name: ").capitalize()
print(name, file=out_file)
out_file.close()

input_file = open("name.txt", 'r')
name = input_file.read()
print("Your name is {}".format(name))
input_file.close()

number_file = open("numbers.txt", 'r')
result = 0
for line_str in number_file:
    number = int(line_str)
    result = result + number
print(result)
number_file.close()
