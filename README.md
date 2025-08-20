# Demo Repository: Snake Game and GitHub Helper Scripts

A simple terminal-based Snake game implemented in Python using the curses library, plus helper scripts/instructions for creating and pushing a GitHub repository.

## Repository Overview

This repository contains:
- A playable Snake game for the terminal (curses-based)
- A shell script that guides you through creating a GitHub repository and pushing your local code
- A text guide with manual GitHub push instructions and troubleshooting tips

## Project Structure

- `snake_game.py` — The game implementation using Python and curses.
- `README.md` — This documentation explaining the repo and how to use it.
- `create_github_repo.sh` — Interactive script to help you create and push a GitHub repository named `Demo`.
- `github_instructions.txt` — Manual instructions for pushing to GitHub and verifying your remote.

## Requirements

- Python 3.x
- curses library
  - Unix/Linux/macOS: included with the Python standard library
  - Windows: install `windows-curses`

To install the Windows dependency:
```
pip install windows-curses
```

## How to Run the Snake Game

1) From the project root, run:
```
python snake_game.py
```

2) Follow the on-screen prompts:
- The program first prints messages in the console and asks you to press Enter to start.
- Inside the game (curses screen), you may see a couple of debug messages like "Starting main function..." and "Screen dimensions: ..." that require pressing any key to proceed.
- Then the game will display "Game is about to start. Press any key to begin..." — press any key to start.

3) Controls:
- Arrow keys (↑, ↓, ←, →) to steer the snake
- Press Ctrl+C to abort immediately (or lose by hitting a wall/yourself)

4) Gameplay:
- Food is shown as the character `O`
- Each food eaten increases your score by 1 and grows the snake
- Game over occurs if the snake hits the edges of the screen or its own body

Tips:
- Ensure your terminal window is sufficiently large; the game checks edges and may error if the window is too small.

## Troubleshooting

- curses.error: If you see messages about a curses error or a hint that the terminal is too small, resize your terminal to be larger and run again.
- Windows: If you get `ModuleNotFoundError: No module named '_curses'`, install `windows-curses` as shown above.
- TERM variable: The game sets a default `TERM` of `xterm-256color` for better compatibility. If your terminal behaves oddly, ensure your environment supports this or set a compatible TERM.

## Customization (Optional)

- Game speed: The refresh rate is controlled by `timeout(100)` (milliseconds). Lower values make the game faster; higher values make it slower.
- Food character: In `snake_game.py`, change `ord('O')` to another character (e.g., `ord('*')`).
- Remove debug pauses: Remove (or comment out) the `getch()` calls that pause before the game starts if you prefer an immediate start.

## Creating and Pushing a GitHub Repository

Recommended (scripted) approach:
1. Ensure you have a GitHub account and you are logged in via your web browser.
2. From the project root, make the script executable and run it:
```
./create_github_repo.sh
```
3. Follow the prompts. The script will guide you to create a repository named `Demo` and then push your local code to it.

Manual approach:
- See `github_instructions.txt` for step-by-step commands (`git remote add`, `git branch -M main`, `git push -u origin main`) and verification using `git remote -v`.

## Notes

- This repository does not include automated tests.
- No explicit license file is provided. Add one if you plan to distribute or collaborate publicly.

Enjoy the game!
