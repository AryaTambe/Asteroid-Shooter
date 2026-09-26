# 🚀 Asteroid Shooter

A simple 2D space shooter game developed using **Python** and **Pygame** as a college semester project.

The player controls a spaceship, shoots falling asteroids, earns points, and tries to survive through **3 levels**. Each level increases the difficulty, and the final level introduces a simple rule-based enemy AI that makes the asteroid track the player's horizontal position.

## 🎮 Game Features

* 3 levels with increasing difficulty
* Player movement
* Shooting system
* Random asteroid generation
* Collision detection
* Score and lives system
* Basic rule-based enemy AI in Level 3
* Sound effects
* Game Over and Win screens
* Restart option
* Modular Python code structure

## 🧠 AI in Level 3

Level 3 includes a simple rule-based AI.

The asteroid compares its horizontal position with the player's position and moves toward the player while continuing to fall.

## 🛠️ Technologies Used

* Python 3
* Pygame
* Object-Oriented Programming
* Collision Detection
* Basic Rule-Based AI

## 📂 Project Structure

```text
Asteroid-Shooter/
├── main.py
├── game.py
├── settings.py
├── player.py
├── bullet.py
├── asteroid.py
├── level.py
├── collision.py
├── ui.py
├── sound.py
└── assets/
    ├── images/
    │   ├── asteroid.png
    │   └── space_background.png
    └── sounds/
        ├── shoot.wav
        ├── game_over.wav
        └── win.wav
```

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AryaTambe/Asteroid-Shooter.git
```

### 2. Open the Project Folder

```bash
cd Asteroid-Shooter
```

### 3. Install Pygame

Make sure Python 3 is installed, then run:

```bash
pip install pygame
```

### 4. Run the Game

```bash
python main.py
```

## 🎮 Controls

| Key         | Action                        |
| ----------- | ----------------------------- |
| Left Arrow  | Move left                     |
| Right Arrow | Move right                    |
| Space       | Shoot                         |
| R           | Restart after Game Over / Win |

## 🏆 How to Play

1. Move the spaceship left and right.
2. Press **Space** to shoot asteroids.
3. Destroy asteroids to increase your score.
4. Avoid collisions with asteroids.
5. You start with **3 lives**.
6. Reach **10 points** to enter Level 2.
7. Reach **20 points** to enter Level 3.
8. Reach **30 points** to win the game.
9. Losing all 3 lives results in Game Over.
10. Press **R** to restart.

## 📈 Levels

### Level 1

Basic falling asteroids with low speed.

### Level 2

Asteroids become faster and appear more frequently.

### Level 3

Asteroids become faster and use a simple tracking AI to move toward the player's horizontal position.

## 👨‍💻 Project Information

**Project:** Asteroid Shooter
**Language:** Python
**Framework:** Pygame
**Type:** 2D Arcade Shooter
**Purpose:** College Semester Project

## 👤 Author

**Arya Tambe**

GitHub: https://github.com/AryaTambe
