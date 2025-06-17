#!/usr/bin/env python3
import curses
import random
import time

def main(stdscr):
    # Debug: Print when main function starts
    stdscr.clear()
    stdscr.addstr(0, 0, "Starting main function...")
    stdscr.refresh()
    stdscr.getch()  # Wait for user input before continuing

    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(100)  # Refresh rate in ms

    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()

    # Debug: Print screen dimensions
    stdscr.clear()
    stdscr.addstr(0, 0, f"Screen dimensions: {sh}x{sw}")
    stdscr.refresh()
    stdscr.getch()  # Wait for user input before continuing

    # Create a new window
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Initial snake position (middle of the screen)
    snake_x = sw // 4
    snake_y = sh // 2

    # Initial snake body
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # Initial food position
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], ord('O'))

    # Initial direction
    key = curses.KEY_RIGHT

    # Score
    score = 0

    # Debug: Print when game is about to start
    w.clear()
    w.addstr(0, 0, "Game is about to start. Press any key to begin...")
    w.refresh()
    w.getch()  # Wait for user input before starting the game

    # Game loop
    while True:
        # Get next key
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Calculate new head position
        new_head = [snake[0][0], snake[0][1]]

        # Check direction and move
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Insert new head
        snake.insert(0, new_head)

        # Check if game over
        if (
            new_head[0] in [0, sh - 1] or
            new_head[1] in [0, sw - 1] or
            new_head in snake[1:]
        ):
            w.clear()
            w.addstr(sh // 2, sw // 2 - 10, f"Game Over! Your score: {score}")
            w.refresh()
            time.sleep(2)
            break

        # Check if snake ate the food
        if snake[0] == food:
            # Increase score
            score += 1

            # Create new food
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], ord('O'))
        else:
            # Remove tail
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Draw snake head
        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

        # Display score
        w.addstr(0, sw - 15, f"Score: {score}")

        # Refresh screen
        w.refresh()

if __name__ == "__main__":
    print("Junie say hello world")
    print("Starting Snake game...")
    print("IMPORTANT: Make sure your terminal window is large enough for the game.")
    print("Press Enter to start the game...")
    input()  # Wait for user to press Enter

    try:
        # Initialize curses
        print("Initializing curses...")
        # Set up the terminal
        import os
        os.environ.setdefault('TERM', 'xterm-256color')

        # Run the game
        curses.wrapper(main)
        print("Game loop ended normally")
    except KeyboardInterrupt:
        print("Game terminated by user")
    except curses.error as e:
        print(f"Curses error: {e}")
        print("This might be due to a terminal window that's too small.")
        print("Please resize your terminal window and try again.")
    except Exception as e:
        import traceback
        print(f"An error occurred: {e}")
        print("Traceback:")
        traceback.print_exc()
    finally:
        print("Thanks for playing Snake!")
