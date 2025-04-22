# collection = single variable used to store multiple values
# List = [] ordered and changeable. Duplicated OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = ()  ordered and unchangeable. Duplicated OK. FASTER


#LISTS : 
fruits = ["apple","orange","banana","coconut"]
# print(dir(fruits))  #print methods and attributes of the fruits.
# print(help(fruits)) # description of methods and attributes

fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0,"mango")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.count("coconut"))


#SETS :

brands = {"samsung","apple","oppo","asus"}

#print(brands[0])   # error -> as the sets are unordered.
brands.add("realme")
brands.remove("apple")
brands.pop()  # first element removed, randomly though


# TUPLE
cars = ("mercedes","bmw")

print(cars.index("bmw"))
print(cars.count("mercedes"))


num_pad = ((1,2,3),(4,5,6),(7,8,9),("*","0","#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()