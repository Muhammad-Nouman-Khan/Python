#A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Adding New Key-Value Pairs

alien_0 = {'color' : 'green','points' : 5}
print(alien_0)
alien_0['x_position'] = 0;
alien_0['y_position'] = 25;
print(alien_0)


#Modifying Values in a Dictionary 

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)



#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) will give error
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)



#Looping Through All Key-Value Pairs
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#******************************************************

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")




#Looping Through All the Keys in a Dictionary

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language.title()}!")


#***********************************************************
#Looping Through a Dictionary’s Keys in a Particular Order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#***********************************************************
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


#A List in a Dictionary

pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
 print("\t" + topping)


#*********************************************************

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


#A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
 }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")