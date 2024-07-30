
# https://pynative.com/python-object-oriented-programming-oop-exercise/
# Link to te web from where I am working on

# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    # this is called a class attribute
    colour = "white"

    def __init__(self, brand, model, max_speed, mileage):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.mileage = mileage

    def brand_model(self):
        return self.brand, self.model

    def max_speed(self):
        return self.max_speed

    def mile_age(self):
        return self.mileage

    def vehicle_capacity(self, capacity=50):
        return f"The capacity of {self.brand} {self.model} is {capacity} passengers"

    def vehicle_colour(self):
        return self.colour


# Create a child class Bus that will inherit all the variables and methods of the Vehicle class


class Bus(Vehicle):
    pass


my_car = Vehicle("Fiat", "500", 200, 5000)
print(my_car.brand_model())
print(my_car.mileage)
print('\n')
my_bus = Bus("Mercedes Benz", "300", 150, 1000)
my_bus.colour = "RED"
print(my_bus.mile_age())
print(my_bus.mileage, "\n")
print(my_bus.vehicle_capacity(capacity=30))
print(my_bus.vehicle_colour())

my_bus_two = Bus("volvo", "600", 160, 300000)
print(my_bus_two.vehicle_colour())
print(my_bus_two.colour)
