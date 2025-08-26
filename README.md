# 🐾 Animals and Vehicles Movement Simulator

A Python program demonstrating polymorphism and object-oriented programming principles through various animals and vehicles that all implement a `move()` method differently.

## 🌟 Features

- **Polymorphism**: Multiple classes implementing the same `move()` method differently
- **Abstract Base Class**: Ensures all subclasses implement the required interface
- **Diverse Categories**: Includes animals, vehicles, and even a robot
- **Interactive Demo**: User can select which objects to move
- **Special Abilities**: Each class has unique additional methods beyond movement

## 🚀 How It Works

The program uses an abstract base class `Movable` that defines the `move()` method. Each subclass implements this method differently:

- **Cheetah**: "Running at 75 mph! 🐆"
- **Dolphin**: "Swimming gracefully 🐬"
- **Eagle**: "Soaring high in the sky 🦅"
- **Car**: "Driving on the road 🚗"
- **Plane**: "Flying through the clouds ✈️"
- **Boat**: "Sailing on water ⛵"
- **Bicycle**: "Pedaling on the path 🚴"
- **Robot**: "Rolling on wheels while beeping 🤖"

## 📋 Requirements

- Python 3.6+
- No external dependencies

## 🛠️ Installation

1. Clone or download the Python file
2. Ensure you have Python installed on your system
3. Run the program with:

```bash
python movement_simulator.py
```

## 🎮 Usage

When you run the program, you'll see:

1. An automatic demonstration of all objects moving
2. A display of each object's special abilities
3. An interactive menu where you can select which object to move

Follow the on-screen prompts to interact with different objects.

## 🧩 Code Structure

- `Movable`: Abstract base class with `move()` method
- Animal classes: `Cheetah`, `Dolphin`, `Eagle`
- Vehicle classes: `Car`, `Plane`, `Boat`, `Bicycle`
- `Robot`: Special class that also implements `move()`
- Helper functions: `make_them_move()`, `demonstrate_special_abilities()`
- Main program with interactive menu

## 💡 Learning Objectives

This code demonstrates:
- Polymorphism in object-oriented programming
- Abstract base classes and method overriding
- Class inheritance and specialization
- User interaction and menu systems
- Clean code organization and separation of concerns

## 📝 Example Output

```
🐾 ANIMALS AND VEHICLES MOVEMENT SIMULATOR 🚀
==================================================
🚀 Making everything move!
========================================
Cheetah: Running at 75 mph! 🐆
Dolphin: Swimming gracefully 🐬
Eagle: Soaring high in the sky 🦅
Car: Driving on the road 🚗
Plane: Flying through the clouds ✈️
Boat: Sailing on water ⛵
Bicycle: Pedaling on the path 🚴
Robot: Rolling on wheels while beeping 🤖
```


## 🤝 Contributing

Feel free to fork this project and add your own movable objects with creative movement implementations!
