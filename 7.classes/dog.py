class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")


dog = Dog("name",3)

print(dog.name)
print(dog.age)
dog.sit()
dog.roll_over()
dog.name = "Max"
print(dog.name)
