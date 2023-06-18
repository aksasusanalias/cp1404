name = input("Enter your name: ")  # Prompt the user for their name
file_name = name + ".txt"
output_file = open(file_name, 'w')
output_file.write(name)  # Write the name to the file
output_file.close()

name_file = open(file_name, 'r')
name_in_file = name_file.read()
print("Your name is", name_in_file)
name_file.close()

file_name = "numbers.txt"

number_file = open(file_name, 'r')
number_1 = int(number_file.readline())
number_2 = int(number_file.readline())
result = number_1 + number_2
print("The result is:", result)


file = open(file_name, 'r')
total = 0
for line in file:
    number = int(line)
    total += number
print("The total is:", total)

