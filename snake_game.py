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
import sys
import tty
import termios

class SnakeGame:
    def __init__(self):
        self.snake_position = [(5, 5)]  # Initial snake position
        self.food_position = (10, 10)   # Initial food position
        self.direction = 'RIGHT'        # Initial direction
        self.game_over = False

    def read_input(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def change_direction(self, key):
        if key == 'w' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif key == 's' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif key == 'a' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif key == 'd' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def game_loop(self):
        while not self.game_over:
            key = self.read_input()
            self.change_direction(key)
            # TODO: Implement the rest of the game logic
            # Update snake position, check for collisions, place new food, etc.

if __name__ == '__main__':
    game = SnakeGame()
    game.game_loop()
import random
import curses

def create_food(snake, box):
    food = None
    while food is None:
        food = [random.randint(box[0][0]+1, box[1][0]-1), random.randint(box[0][1]+1, box[1][1]-1)]
        if food in snake:
            food = None
    return food

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3, sw-3]]
    snake = [[sh//2, sw//2 + 1], [sh//2, sw//2], [sh//2, sw//2 - 1]]
    direction = curses.KEY_RIGHT

    for y, x in box:
        stdscr.addch(y, x, '+')

    food = create_food(snake, box)
    stdscr.addch(food[0], food[1], '#')

    score = 0

    while True:
        next_key = stdscr.getch()
        direction = direction if next_key == -1 else next_key

        head = [snake[0][0], snake[0][1]]

        if direction == curses.KEY_DOWN:
            head[0] += 1
        if direction == curses.KEY_UP:
            head[0] -= 1
        if direction == curses.KEY_LEFT:
            head[1] -= 1
        if direction == curses.KEY_RIGHT:
            head[1] += 1

        snake.insert(0, head)

        if snake[0] == food:
            score += 1
            food = create_food(snake, box)
            stdscr.addch(food[0], food[1], '#')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1]  in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]):
            break

        stdscr.addch(snake[0][0], snake[0][1], '*')

    stdscr.addstr(sh//2, sw//2 - len("Game Over!")//2, "Game Over!")
    stdscr.nodelay(0)
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
