# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)

# print(motorcycles[-1])   # print the last value

# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles.insert(0,'BMW')
# print(motorcycles)

# del(motorcycles[0])
# print(motorcycles)

# popped_motorcyle = motorcycles.pop()   #removes the last
# print(motorcycles)
# print(popped_motorcyle)

# last_owned = popped_motorcyle
# print(f"The last motorcycle I owned was a {last_owned}")

# first_owned = motorcycles.pop(0)   #Popping Items from any Position in a List
# print(f"The first motorcycle I owned was a {first_owned}")


# print(motorcycles)

# too_expensive = 'suzuki'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")


# cars = ['bmw','audi','toyota','subaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# print(sorted(cars))  #Sorting a List Temporarily with the sorted() Function
# print(cars)

# cars.reverse()   #Printing a List in Reverse Order
# print(cars)

# print(len(cars))


# WORKING WITH LISTS

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# print("Thank you, everyone. That was a great magic show!\n")

# print("****************************")

# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# print(f"I can't wait to see your next trick, {magician.title()}.\n")

# print("****************************")

#************************************************************

# Using the range() Function

for value in range(1,5):
    print(value)

#Using range() to Make a List of Numbers

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value ** 2 for value in range(1,11)]
print(squares)


players = ['ronaldo','messi','neymar','mbappe','kane']
print(players[0:3])

print(players[:4])

print(players[2:])

print(players[-3:])   #print last three players



#Copying a List

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)


# now both points to the same list, change in one, affects the other.
my_foods = friend_foods

my_foods.append('rice')
friend_foods.append('biryani')

print(my_foods)
print(friend_foods)

# Defining a Tuple (same as lists, only diff is: values cant be changed)

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250   # ERROR !!!


# if tuple with only one element : 
my_t = (3,)
print(my_t[0])


#You cannot modify a tuple, but you can assign a new value to a variable that represents a tuple.

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)