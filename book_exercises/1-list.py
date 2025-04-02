magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

#Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)


cubes = []
for number in range(1,11):
    cubes.append(number**3)

print(cubes)

#cube comprehension
cubes = [number**3 for number in range(1,11)];
print(cubes)



#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[-3:])


#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#if this :
# friend_foods = my_foods (change in one affect the other too...)



#Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250  (cant change, gives error)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)