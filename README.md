# Asteroids Game

A classic arcade-style asteroids game built with Python and Pygame. Navigate your spaceship through an asteroid field, shoot asteroids to break them into smaller pieces, and survive as long as possible!

## Features

- **Player Movement**: Rotate and thrust your triangular spaceship
- **Asteroid Physics**: Large asteroids split into smaller ones when shot
- **Collision Detection**: Circular collision detection between all game objects
- **Smooth Controls**: 60 FPS gameplay with responsive controls
- **Shooting System**: Fire projectiles to destroy asteroids

## Screenshots

### Main Menu
<img width="1356" height="817" alt="image" src="https://github.com/user-attachments/assets/afb595a1-472e-4c21-86f7-30b2ed7fb7e2" />

### Game Play
<img width="1356" height="817" alt="image" src="https://github.com/user-attachments/assets/6a9cb975-33d9-4f6c-9abb-73c7cff535b1" />

### Game Over Screen
<img width="1356" height="817" alt="image" src="https://github.com/user-attachments/assets/83cbb6e7-841a-4f8f-9db5-c42490fd56e5" />

## Installation

This project uses pygame and a virtual environment for development. Follow these steps to set up and run the game:

### Prerequisites
- Python 3.6+ installed on your system
- `uv` package manager (install from [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/))

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aott33/asteroids-game.git
   cd asteroids-game
   ```

2. **Create a virtual environment:**
   ```bash
   uv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```
   
   You should see `(asteroids-game)` at the beginning of your terminal prompt.

4. **Install pygame dependency:**
   ```bash
   uv add pygame==2.6.1
   ```

5. **Verify pygame installation:**
   ```bash
   uv run -m pygame
   ```
   
   This will show an error (expected) but confirm pygame 2.6.1 is installed.

6. **Run the game:**
   ```bash
   python main.py
   ```

### Additional Notes

- **WSL Users**: If you're using Windows Subsystem for Linux, you may need to install VcXsrv to run pygame applications with GUI support.
- **Virtual Environment**: Make sure your virtual environment is activated (you should see the project name in your terminal prompt) when running the game.
- **Dependencies**: This project uses pygame 2.6.1 specifically. The virtual environment keeps this isolated from other Python projects on your system.

## Controls

- **A** or **Left Arrow**: Rotate ship counterclockwise
- **D** or **Right Arrow**: Rotate ship clockwise  
- **W** or **Up Arrow**: Thrust forward
- **S** or **Down Arrow**: Thrust backward
- **Spacebar**: Shoot
- **ESC** or **Close Window**: Quit game

## Game Mechanics

### Player Ship
- Triangular spaceship that can rotate 360 degrees
- Thrust in the direction you're facing
- Circular hitbox for collision detection

### Asteroids
- Start as large asteroids that drift across the screen
- When shot, large asteroids split into 2 medium asteroids
- Medium asteroids split into 2 small asteroids
- Small asteroids are destroyed completely when shot
- Split asteroids move faster than their parent

### Shooting
- Press spacebar to fire projectiles
- Shots travel in straight lines at high speed
- Cooldown system prevents rapid-fire shooting

### Collision
- Game ends when player collides with an asteroid
- Shots destroy asteroids on impact

## Project Structure

```
asteroids-game/
├── main.py              # Main game loop and initialization
├── player.py            # Player ship class
├── asteroid.py          # Asteroid class with splitting logic
├── shot.py              # Projectile class
├── circleshape.py       # Base class for circular collision detection
├── asteroidfield.py     # Asteroid spawning system
├── constants.py         # Game configuration and constants
└── README.md           # This file
```

## Technical Details

- **Engine**: Built with Pygame
- **Physics**: Custom vector-based movement and collision system
- **Architecture**: Object-oriented design with sprite groups
- **Graphics**: Simple geometric shapes drawn with Pygame primitives

## Todo

- [x] Add a menu (when game over, show game over then after 10s go to menu)
- [x] Add a scoring system
- [ ] Implement multiple lives and respawning
- [ ] Add an explosion effect for the asteroids
- [ ] Add acceleration to the player movement
- [x] Make the objects wrap around the screen instead of disappearing (just player)
- [ ] Create different weapon types
- [ ] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped

## Contributing

Feel free to fork this project and submit pull requests with improvements or new features!

## Acknowledgments

- Inspired by the classic Atari Asteroids arcade game

- Built as a learning project for [boot.dev](boot.dev)



