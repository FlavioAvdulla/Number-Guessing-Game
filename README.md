# Number Guessing Game

A visually appealing number guessing game built with Pygame where players try to guess a randomly generated number between 1 and 100.

## Features
- Clean, modern UI with a dark theme and blue accents
- Interactive input box for number guesses
- Visual feedback on guesses (too high/too low)
- Attempt counter to track progress
- Play again functionality
- Responsive buttons with hover effects

## Requirements
- Python 3.x
- Pygame library

## Installation

1. Clone or download this repository

2. Install Pygame if you don't have it already:

```
pip install pygame
```
3. Run the game:

```
python number_guessing_game.py
```

## How to Play

1. The game generates a random number between 1 and 100

2. Enter your guess in the input box (3-digit maximum)

3. Click "Submit Guess" or press Enter to submit your guess

4. The game will tell you if your guess is too high or too low

5. Keep guessing until you find the correct number

6. Click "Play Again" to start a new game after winning

## Game Screenshot


## File Structure
text
number-guessing-game/
├── number_guessing_game.py  # Main game file
└── README.md                # This file

## Code Overview
The game implements several classes:

Button: Handles interactive buttons with hover effects

InputBox: Manages text input with validation

Main game loop handles events, updates game state, and renders the UI

## Customization
You can easily customize:

Colors by modifying the color constants

Window size by changing WIDTH and HEIGHT

Number range by modifying the generate_secret_number() function

Fonts and sizes by adjusting the font variables