# Snake Game

A simple terminal-based Snake game implemented in Python using the curses library.

## Description

This is a classic Snake game where you control a snake that moves around the screen. The objective is to eat food (O symbols) to grow longer while avoiding collisions with the walls and yourself.

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

2. Initial Setup:
   - The game will display some initial messages and prompt you to press Enter to start
   - There will be a few debug screens showing the game initialization - press any key to proceed through them

3. Controls:
   - Use arrow keys (↑, ↓, ←, →) to control the snake's direction
   - Press Ctrl+C to exit the game

4. Rules:
   - Eat food (O symbols) to grow longer and increase your score
   - Avoid hitting the walls or your own body
   - The game ends when you collide with a wall or yourself
   - Your final score will be displayed when the game ends

## Installation for Windows Users

If you're using Windows, you'll need to install the windows-curses package:

```
pip install windows-curses
```

## GitHub Repository

To create a GitHub repository for this project and push the code:

1. Make sure you have a GitHub account.
2. Run the provided script:
   ```
   ./create_github_repo.sh
   ```
3. Follow the instructions in the script to create a repository called Demo and push the code to it.

Alternatively, you can follow the instructions in the `github_instructions.txt` file, which contains:
- Detailed manual steps for creating a GitHub repository
- Troubleshooting tips if you can't see your repository
- Instructions for verifying that your repository was set up correctly

## Troubleshooting

If you encounter issues when running the game:

- Make sure your terminal window is large enough - the game will display an error if the window is too small
- If you get a curses error, try resizing your terminal window and running the game again
- The game includes error handling that will display helpful messages if something goes wrong

## Enjoy the game!
