friends = 0
friends += 1  #argumented assignment operator
print(friends)

friends = 5
friends = friends ** 2  # 5^2 = 25 (power)
print(friends)

x = 3.14
y = -4
z = 5

result = round(x)
print(result)  # prints 3

result = abs(y)  
print(result)  # prints 4

result = pow(4,3)
print(result)  # prints 64

result = max(x,y,z)
print(result)  # 5

result = min(x,y,z)
print(result)  # -4

# Math Library :
import math

print(math.pi)

print(math.e)

x = 9

result = math.sqrt(x)

print(result) #3.0

y = 9.2

result = math.ceil(y)

print(result) #10

result = math.floor(y);
print(result)  #9


# EXERCISE c = underroot(a^2 + b^2)

a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = math.sqrt(pow(a,2) + pow(b,2));
print(f"c = {round(c,2)}")

