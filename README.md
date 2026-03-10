# Penguin Academy - OOP Simulation System

## Overview
This project is a console-based simulation system developed in Python, focusing heavily on **Object-Oriented Programming (OOP)** architecture and system design. The core objective of this project is to demonstrate the ability to build scalable, modular software with a clear separation of concerns, moving away from procedural scripts into structured, object-oriented modeling.

## System Architecture
The codebase is strictly divided into three logical layers to ensure extensibility and maintainability. This design allows the application to grow without breaking existing functionality.

1. **Domain Layer (`dominio.py`):** The core business logic. Contains all entities, rules, and states. 
2. **Engine Layer (`motor.py`):** The orchestrator. Manages the Game Loop, coordinates turns, and evaluates win/loss conditions. It contains no display logic.
3. **UI Layer (`ui.py`):** The presentation layer. Solely responsible for rendering information to the console, keeping the engine completely agnostic of the presentation method.

## OOP Principles Applied
- **Abstraction:** Implemented an abstract base class using Python's `abc` module to define a strict contract for all character types in the system.
- **Encapsulation:** Protected critical state variables (e.g., health, energy, core structure integrity) using private attributes. State mutation is strictly controlled through dedicated methods to prevent external interference.
- **Inheritance:** Created specialized child classes (`PinguinoIngeniero`, `PinguinoGuerrero`, `PinguinoExplorador`) that inherit base attributes and behaviors from the parent class, promoting DRY (Don't Repeat Yourself) principles.
- **Polymorphism:** Overrode the abstract `ejecutar_accion()` method in each child class. The game engine interacts with all entities uniformly, delegating the specific behavior to the objects themselves.

## Project Structure
```text
├── main.py       # Application entry point (Dependency injection and initialization)
├── motor.py      # Game engine and loop controller
├── dominio.py    # Abstract base classes and concrete implementations
└── ui.py         # Console rendering interface