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
# Modifying an attribute's value directly
dog.name = "Max"
print(dog.name)


# **************************

class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Filling the gas tank.")



#  INHERITANCE 

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    # Overriding a method from the parent class
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

my_tesla = ElectricCar("tesla","model s",2019)

print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()

my_tesla.fill_gas_tank()

