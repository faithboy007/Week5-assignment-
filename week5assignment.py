from abc import ABC, abstractmethod
from typing import List

# Abstract base class
class Movable(ABC):
    @abstractmethod
    def move(self):
        pass
    
    def describe(self):
        return f"{self.__class__.__name__} is moving"

# Animal classes
class Cheetah(Movable):
    def move(self):
        return "Running at 75 mph! 🐆"
    
    def describe(self):
        return "Fastest land animal"

class Dolphin(Movable):
    def move(self):
        return "Swimming gracefully 🐬"
    
    def hunt(self):
        return "Hunting for fish with echolocation"

class Eagle(Movable):
    def move(self):
        return "Soaring high in the sky 🦅"
    
    def move_altitude(self, feet):
        return f"Soaring at {feet} feet above ground"

# Vehicle classes
class Car(Movable):
    def move(self):
        return "Driving on the road 🚗"
    
    def honk(self):
        return "Beep beep! 🚨"

class Plane(Movable):
    def move(self):
        return "Flying through the clouds ✈️"
    
    def takeoff(self):
        return "Taking off from runway 🛫"

class Boat(Movable):
    def move(self):
        return "Sailing on water ⛵"
    
    def anchor(self):
        return "Dropping anchor ⚓"

class Bicycle(Movable):
    def move(self):
        return "Pedaling on the path 🚴"
    
    def ring_bell(self):
        return "Ring ring! 🔔"

# Robot class (just for fun)
class Robot(Movable):
    def move(self):
        return "Rolling on wheels while beeping 🤖"
    
    def speak(self):
        return "Beep boop. I am a robot."

# Function to demonstrate polymorphism
def make_them_move(movables: List[Movable]):
    print("🚀 Making everything move!")
    print("=" * 40)
    
    for movable in movables:
        print(f"{movable.__class__.__name__}: {movable.move()}")
    print()

# Function to show additional behaviors
def demonstrate_special_abilities():
    cheetah = Cheetah()
    dolphin = Dolphin()
    eagle = Eagle()
    car = Car()
    plane = Plane()
    boat = Boat()
    bicycle = Bicycle()
    robot = Robot()
    
    # Show special abilities
    abilities = [
        ("Cheetah", cheetah.describe()),
        ("Dolphin", dolphin.hunt()),
        ("Eagle", eagle.move_altitude(10000)),
        ("Car", car.honk()),
        ("Plane", plane.takeoff()),
        ("Boat", boat.anchor()),
        ("Bicycle", bicycle.ring_bell()),
        ("Robot", robot.speak())
    ]
    
    print("🌟 Special Abilities:")
    print("=" * 40)
    for name, ability in abilities:
        print(f"{name}: {ability}")
    print()

# Main program
def main():
    # Create instances of different movable objects
    movables = [
        Cheetah(),
        Dolphin(),
        Eagle(),
        Car(),
        Plane(),
        Boat(),
        Bicycle(),
        Robot()
    ]
    
    print("🐾 ANIMALS AND VEHICLES MOVEMENT SIMULATOR 🚀")
    print("=" * 50)
    
    # Demonstrate polymorphism
    make_them_move(movables)
    
    # Show special abilities
    demonstrate_special_abilities()
    
    # Interactive demonstration
    print("🎯 Interactive Demonstration:")
    print("=" * 30)
    
    # Let user choose which objects to move
    objects_dict = {
        '1': Cheetah(),
        '2': Dolphin(),
        '3': Eagle(),
        '4': Car(),
        '5': Plane(),
        '6': Boat(),
        '7': Bicycle(),
        '8': Robot(),
        '9': "Exit"
    }
    
    while True:
        print("\nChoose an object to move:")
        for key, obj in objects_dict.items():
            if key == '9':
                print(f"{key}. {obj}")
            else:
                print(f"{key}. {obj.__class__.__name__}")
        
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == '9':
            print("Goodbye! 👋")
            break
        elif choice in objects_dict and choice != '9':
            selected = objects_dict[choice]
            print(f"\n🎬 {selected.__class__.__name__} action: {selected.move()}")
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()