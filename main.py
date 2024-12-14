# Activity 1

# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level  # Encapsulation: private attribute
    
    def turn_on(self):
        return f"{self.brand} {self.model} is turning on."
    
    def turn_off(self):
        return f"{self.brand} {self.model} is turning off."

    # Method to access the battery level
    def check_battery(self):
        return f"Battery level is {self.__battery_level}%"
    
    # Method to simulate charging
    def charge(self, amount):
        self.__battery_level += amount
        if self.__battery_level > 100:
            self.__battery_level = 100
        return f"Charging... Battery is now {self.__battery_level}%"

# Derived class: AdvancedSmartphone (demonstrating inheritance and overriding)
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, battery_level, camera_quality):
        super().__init__(brand, model, battery_level)  # Call parent class constructor
        self.camera_quality = camera_quality  # New attribute for advanced smartphones
    
    def take_photo(self):
        return f"Taking a photo with {self.camera_quality} camera."

    # Override the turn_on method
    def turn_on(self):
        return f"{self.brand} {self.model} with {self.camera_quality} camera is turning on."

# Creating an object of AdvancedSmartphone
smartphone = AdvancedSmartphone("Samsung", "Galaxy S23", 80, "108MP")

# Interact with the object
print(smartphone.turn_on())  # Overridden method
print(smartphone.check_battery())  # Encapsulation in action
print(smartphone.take_photo())  # Method from the derived class
print(smartphone.charge(15))  # Charging the phone

# Activity 2

# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# List of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action
for vehicle in vehicles:
    print(vehicle.move())
