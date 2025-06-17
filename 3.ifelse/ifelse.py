banned_users = ['nouman','umar','qasim']
user = 'ali'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
print("*********************************")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("*********************************")

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")


print("*********************************")

#Using if Statements with Lists

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\n Finished making your pizza!")

print("*********************************")

