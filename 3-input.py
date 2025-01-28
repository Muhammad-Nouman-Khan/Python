#input() = A function that prompts the user to enter data, Returns the entered data as a string

name = input("Enter your name : ");
age = input("Enter your age : ");

age = int(age);

age = age + 1;

print(f"Hello {name}!");

print(f"You are {age} years old");

