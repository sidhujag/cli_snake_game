import sys
import tty
import termios
import time
from enum import Enum, auto

# Define the possible directions
class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

# Initialize the game state
class GameState:
    def __init__(self):
        self.snake = [(5, 5), (5, 4), (5, 3)]
        self.direction = Direction.RIGHT
        self.food = (10, 10)
        self.width = 30
        self.height = 20
        self.score = 0
        self.game_over = False

# Function to get a keypress
def get_keypress():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Function to update the game state
def update_game_state(state):
    head_x, head_y = state.snake[0]
    if state.direction == Direction.UP:
        head_y -= 1
    elif state.direction == Direction.DOWN:
        head_y += 1
    elif state.direction == Direction.LEFT:
        head_x -= 1
    elif state.direction == Direction.RIGHT:
        head_x += 1

    # Check for game over conditions
    if (head_x, head_y) in state.snake or head_x < 0 or head_y < 0 or head_x >= state.width or head_y >= state.height:
        state.game_over = True
        return

    # Move the snake
    state.snake.insert(0, (head_x, head_y))

    # Check for food collision
    if (head_x, head_y) == state.food:
        state.score += 1
        # For simplicity, food reappears at the same spot
        # In a real game, it should appear at a random location
    else:
        state.snake.pop()

# Function to render the game state
def render_game_state(state):
    for y in range(state.height):
        for x in range(state.width):
            if (x, y) == state.food:
                sys.stdout.write('F')
            elif (x, y) in state.snake:
                sys.stdout.write('*')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')

# Function to handle keypresses and change direction
def handle_keypress(state, key):
    if key == 'w' and state.direction != Direction.DOWN:
        state.direction = Direction.UP
    elif key == 's' and state.direction != Direction.UP:
        state.direction = Direction.DOWN
    elif key == 'a' and state.direction != Direction.RIGHT:
        state.direction = Direction.LEFT
    elif key == 'd' and state.direction != Direction.LEFT:
        state.direction = Direction.RIGHT

# Main game loop
def main():
    state = GameState()
    while not state.game_over:
        render_game_state(state)
        key = get_keypress()
        handle_keypress(state, key)
        update_game_state(state)
        time.sleep(0.1)  # Game tick rate
        sys.stdout.write('\x1b[1;1H\x1b[2J')  # Clear the screen
    print(f"Game Over! Your score was: {state.score}")

if __name__ == "__main__":
    main()
