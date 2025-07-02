with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print("********************")

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip()) #rstrip() method removes, or strips, any whitespace character from the right side of the string.