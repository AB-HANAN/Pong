# Pong by Abdul Hanan

This is a beginner-friendly implementation of the classic Pong game using Python and the Turtle graphics module. The game is a simple 2D tennis game where two players control paddles to hit a ball back and forth across the screen. The first player to miss the ball loses the round.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Controls](#game-controls)
- [Game Structure](#game-structure)
- [License](#license)

## Features

- **Two-player gameplay**: Play against a friend with keyboard controls.
- **Simple graphics**: Built using the Turtle module for easy customization.
- **Sound effects**: Includes sound effects when the ball hits the paddles or the edges.
- **Score tracking**: Keeps track of each player's score.

## Installation

To run this game on your local machine, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pong-game.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd pong-game
   ```

3. **Ensure you have Python installed:**

   This game requires Python 3.x. You can download it from [python.org](https://www.python.org/downloads/).

4. **Install the required libraries:**

   The game uses the Turtle graphics module, which is included in the Python standard library. For sound, it uses the `winsound` module (only works on Windows).

   ```bash
   pip install turtle
   ```

5. **Run the game:**

   ```bash
   python pong.py
   ```

## How to Play

The objective of Pong is to hit the ball past your opponent's paddle to score a point. The first player to reach a certain number of points wins the game.

## Game Controls

- **Player A:**
  - Move Up: `W`
  - Move Down: `S`

- **Player B:**
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`

## Game Structure

### Main Components

- **Window Setup**: The game window is set up with a title, background color, and dimensions.
- **Paddles**: Two paddles are created using the Turtle module, one for each player.
- **Ball**: A ball is created that moves across the screen, bouncing off paddles and the top/bottom edges.
- **Score**: The game keeps track of each player's score, which is displayed at the top of the screen.

### Key Functions

- **Paddle Movement**: Functions to move paddles up and down.
- **Ball Movement**: The ball moves automatically, and its direction changes upon collision with the paddles or the edges of the window.
- **Collision Detection**: The game checks for collisions between the ball and the paddles and changes the ball's direction accordingly.
- **Score Update**: The score is updated when the ball crosses the left or right boundary, indicating a point for the opposite player.

### Sound Effects

The game includes sound effects when the ball hits the paddles or the window edges. Ensure you have the correct path to the sound file (`jump-sound-14839.mp3`) on your machine.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as you like.

---

Feel free to adjust any sections to better fit your specific needs! Let me know if there's anything else you'd like to add.
