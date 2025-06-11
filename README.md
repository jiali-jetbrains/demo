# Snake Game

A simple terminal-based Snake game implemented in Python using the curses library.

## Description

This is a classic Snake game where you control a snake that moves around the screen. The objective is to eat food (π symbols) to grow longer while avoiding collisions with the walls and yourself.

## Features

- Snake movement using arrow keys
- Food generation
- Score tracking
- Game over screen

## Requirements

- Python 3.x
- curses library (included in Python standard library for Unix/Linux/macOS; for Windows, you may need to install windows-curses)

## How to Play

1. Run the game:
   ```
   python snake_game.py
   ```

2. Controls:
   - Use arrow keys (↑, ↓, ←, →) to control the snake's direction
   - Press Ctrl+C to exit the game

3. Rules:
   - Eat food (π symbols) to grow longer and increase your score
   - Avoid hitting the walls or your own body
   - The game ends when you collide with a wall or yourself

## Installation for Windows Users

If you're using Windows, you'll need to install the windows-curses package:

```
pip install windows-curses
```

## Enjoy the game!