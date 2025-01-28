# typecasting = the process of converting a variable from one data type to another str() , int() , float(), bool()

name = "Nouman Khan"
age = 22
gpa = 3.81
is_student = True

print(type(gpa))

gpa = int(gpa)
age = str(age)

age += "1"  #221

print(age)
print(gpa)

name = bool(name)
print(name) #true

name = ""
name = bool(name)
print(name)  #false