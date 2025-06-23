# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")


# *********************************************

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")



# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)




# # Moving Items from One List to Another

# unconfirmed_users = ['nouman','qasim','umar']

# print("\nThe following users are not confirmed:")
# for unconfirmed_user in unconfirmed_users:
#     print(unconfirmed_user.title())

# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: ${current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())



# Removing All Instances of Specific Values from a List

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
 
# print(pets)

# Filling a Dictionary with User Input

responses = {}

polling_active = True

while polling_active:

    name = input("\nWhat's your name ? ")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person response ? (yes/no)")

    if repeat == "no":
        polling_active = False

print("\n---Poll Results---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")