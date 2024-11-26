# Question 1
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self._storage = storage  # Protected attribute
        self.__battery_life = battery_life  # Private attribute

    # Getter for private attribute
    def get_battery_life(self):
        return self.__battery_life

    # Setter for private attribute
    def set_battery_life(self, hours):
        if hours > 0:
            self.__battery_life = hours
        else:
            print("Battery life must be positive.")

    # Method to simulate phone usage
    def use_phone(self, hours):
        if hours <= self.__battery_life:
            self.__battery_life -= hours
            return f"You used your phone for {hours} hours. Remaining battery: {self.__battery_life} hours."
        else:
            return "Not enough battery for this usage."

    # Method to display phone info
    def display_info(self):
        return f"Smartphone: {self.brand} {self.model}, Storage: {self._storage}GB, Battery Life: {self.__battery_life} hours."

# Subclass for Smartwatch (Inheritance)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery_life, fitness_tracking=True):
        super().__init__(brand, model, storage, battery_life)
        self.fitness_tracking = fitness_tracking

    # Overriding the display_info method (Polymorphism)
    def display_info(self):
        tracking = "Enabled" if self.fitness_tracking else "Disabled"
        return f"Smartwatch: {self.brand} {self.model}, Storage: {self._storage}GB, Battery Life: {self.get_battery_life()} hours, Fitness Tracking: {tracking}"

# Example Usage
# Create a Smartphone object
phone = Smartphone("Apple", "iPhone 14", 128, 24)
print(phone.display_info())
print(phone.use_phone(5))
phone.set_battery_life(20)
print(phone.display_info())

# Create a Smartwatch object
watch = Smartwatch("Samsung", "Galaxy Watch 6", 16, 48, fitness_tracking=True)
print(watch.display_info())
print(watch.use_phone(10))


# Question 2
# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Function to demonstrate polymorphism
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(f"{vehicle.__class__.__name__} is {vehicle.move()}.")

# Example usage
car = Car()
plane = Plane()
boat = Boat()

# List of vehicle objects
vehicles = [car, plane, boat]

# Demonstrate polymorphism
demonstrate_movement(vehicles)

