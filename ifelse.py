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

