# Activity 1: Superhero class with inheritance and encapsulation

class Superhero:
    def __init__(self, name, power_level):
        self.name = name
        self._power_level = power_level  # Encapsulated attribute

    def display_info(self):
        print(f"{self.name} has a power level of {self._power_level}.")

    def use_power(self):
        print(f"{self.name} uses their superpower!")


class FlyingHero(Superhero):
    def __init__(self, name, power_level, max_altitude):
        super().__init__(name, power_level)
        self.max_altitude = max_altitude

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.max_altitude} feet!")


class Speedster(Superhero):
    def __init__(self, name, power_level, max_speed):
        super().__init__(name, power_level)
        self.max_speed = max_speed

    def use_power(self):
        print(f"{self.name} runs at an incredible {self.max_speed} mph!")


# Creating objects
hero1 = FlyingHero("SkyBlazer", 95, 10000)
hero2 = Speedster("FlashRush", 90, 500)

# Method calls
hero1.display_info()
hero1.use_power()
print()
hero2.display_info()
hero2.use_power()

# Activity 2

class Vehicle:
    def move(self):
        print("The vehicle moves in a generic way.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road! ")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("Sailing through the water!")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Polymorphism in action


