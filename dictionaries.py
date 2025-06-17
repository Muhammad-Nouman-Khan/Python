alien_0 = {
    'color' : 'green',
    'points': 5
}

new_points = alien_0['points']

print(f"You just earned {new_points} points!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print("*****************************")

alien_0 = {
    'x_position' : 0,
    'y_position' : 25,
    'speed' : 'medium'
}

print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment;
print(f"New position : {alien_0['x_position']}")

del alien_0['speed']
print(alien_0)


print("\n*****************************")


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

nom_fav = favorite_languages.get('nouman','No favourite language assigned')

print(nom_fav)

print("\n*****************************")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key,value in user_0.items():
    print(f"\nKey : {key}")
    print(f"\nValue : {value}")


print("\n*****************************")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name,language in favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

print("\n*****************************")

for name in favorite_languages.keys():
    print(name.title())

print("\n*****************************")

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

print("\n*****************************")

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

print("\n*****************************")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


print("\n*****************************")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


print("\n*****************************")


# LIST OF DICTIONARIES

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


print("\n*****************************")

aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {
        'color' : 'green',
        'points' : 5,
        'speed' : 'slow'
    }

    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")


print("\n*****************************")

# A List in a Dictionary

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings : ")

for topping in pizza['toppings']:
    print("\t" + topping)

print("\n*****************************")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")

    for language in languages:
        print(f"\t{language.title()}")