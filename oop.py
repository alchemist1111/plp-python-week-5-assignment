# Assignment 1: Design Your Own Class!
# Smartphone class
class Smartphone:
    def __init__(self, brand, model, year, battery_life):
        self.brand = brand
        self.model = model
        self.year = year
        self.battery_life = battery_life
        
    def get_details(self):
        return f"{self.brand} {self.model} ({self.year}) - Battery Life: {self.battery_life} hours"
    
    def call(self):
        print(f"Making a call from {self.brand} {self.model}...") 
        
    def play_music(self):
        print(f"Playing music on {self.brand} {self.model}...")


# Inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, year, battery_life, processor_speed):
        super().__init__(brand, model, year, battery_life)
        self.processor_speed = processor_speed
        
    def get_details(self):
        details = super().get_details()
        return f"{details} - Processor Speed: {self.processor_speed} GHz"
    
    def play_game(self):
        print(f"Playing games smoothly on {self.brand} {self.model} with {self.processor_speed} GHz processor...")        
        
# Objects
phone1 = Smartphone("Samsung", "Galaxy S25", 2025, 20)
gaming_phone = GamingPhone("Asus", "ROG Phone 5", 2022, 15, 3.0)

# Accessing methods
print(phone1.get_details())
phone1.call()
phone1.play_music()

print("\nGaming Phone Details:")
print(gaming_phone.get_details())
gaming_phone.call()
gaming_phone.play_music()
gaming_phone.play_game()



# Activity 2: Polymorphism Challenge!
class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("The dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("The bird is flying 🦅")

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️")

# Creating objects
dog = Dog()
bird = Bird()
car = Car()
plane = Plane()

# Calling move() on different objects
dog.move()
bird.move()
car.move()
plane.move()
        