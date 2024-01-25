import random

# Define the possible directions
DIRECTIONS = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}

# Initialize the game state
def initialize_game(width=30, height=20):
    snake = [(width // 2, height // 2)]
    food = create_food(snake, width, height)
    direction = 'RIGHT'
    return {'snake': snake, 'food': food, 'direction': direction, 'width': width, 'height': height, 'game_over': False}

# Function to get a keypress
def create_food(snake, width, height):
    while True:
        food = (random.randint(1, width - 2), random.randint(1, height - 2))
        if food not in snake:
            return food

# Function to update the game state
def move_snake(game_state):
    head_x, head_y = game_state['snake'][0]
    delta_x, delta_y = DIRECTIONS[game_state['direction']]
    new_head = (head_x + delta_x, head_y + delta_y)
    game_state['snake'].insert(0, new_head)
    if new_head == game_state['food']:
        game_state['food'] = create_food(game_state['snake'], game_state['width'], game_state['height'])
    else:
        game_state['snake'].pop()

def check_collision(game_state):
    head = game_state['snake'][0]
    # Check if the snake has hit the wall
    if head[0] <= 0 or head[0] >= game_state['width'] - 1 or head[1] <= 0 or head[1] >= game_state['height'] - 1:
        game_state['game_over'] = True
    # Check if the snake has hit itself
    if head in game_state['snake'][1:]:
        game_state['game_over'] = True

def main():
    game_state = initialize_game()
    while not game_state['game_over']:
        move_snake(game_state)
        check_collision(game_state)
        # TODO: Implement rendering and input handling
        # render_game_state(game_state)
        # handle_input(game_state)
    print("Game Over!")

    # Check for food collision
    if (head_x, head_y) == state.food:
        state.score += 1
        # For simplicity, food reappears at the same spot
        # In a real game, it should appear at a random location
    else:
        state.snake.pop()
    head_x, head_y = state.snake[0]
    if state.direction == Direction.UP:
        head_y -= 1
    elif state.direction == Direction.DOWN:
        head_y += 1
    elif state.direction == Direction.LEFT:
        head_x -= 1
    elif state.direction == Direction.RIGHT:
        head_x += 1

def check_collision(game_state):
    head = game_state['snake'][0]
    # Check if the snake has hit the wall
    if head[0] <= 0 or head[0] >= game_state['width'] - 1 or head[1] <= 0 or head[1] >= game_state['height'] - 1:
        game_state['game_over'] = True
    # Check if the snake has hit itself
    if head in game_state['snake'][1:]:
        game_state['game_over'] = True

def main():
    game_state = initialize_game()
    while not game_state['game_over']:
        move_snake(game_state)
        check_collision(game_state)
        # TODO: Implement rendering and input handling
        # render_game_state(game_state)
        # handle_input(game_state)
    print("Game Over!")

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
    main()

if __name__ == "__main__":
    main()
    main()

if __name__ == "__main__":
    main()
import random

# Define the possible directions
DIRECTIONS = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}

# Initialize the game state
def initialize_game(width=30, height=20):
    snake = [(width // 2, height // 2)]
    food = create_food(snake, width, height)
    direction = 'RIGHT'
    return {'snake': snake, 'food': food, 'direction': direction, 'width': width, 'height': height, 'game_over': False}

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
import random
import curses

def create_snake_and_food(screen_width, screen_height):
    snake = [[screen_height//2, screen_width//4]]
    food = [screen_height//2, screen_width//2]
    return snake, food

def print_score(stdscr, score):
    stdscr.addstr(0, 2, 'Score: ' + str(score))

def game(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.timeout(100)

    screen_height, screen_width = stdscr.getmaxyx()
    snake, food = create_snake_and_food(screen_width, screen_height)

    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, screen_height] or \
           snake[0][1]  in [0, screen_width] or \
           snake[0] in snake[1:]:
            stdscr.addstr(screen_height//2, screen_width//2, "Game Over")
            stdscr.nodelay(0)
            stdscr.getch()
            break

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, screen_height-1),
                    random.randint(1, screen_width-1)
                ]
                food = nf if nf not in snake else None
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(int(tail[0]), int(tail[1]), ' ')

        stdscr.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
        print_score(stdscr, len(snake))

if __name__ == "__main__":
    curses.wrapper(game)
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
    stdscr.box()

    snake = [[sh//2, sw//2 + 1], [sh//2, sw//2], [sh//2, sw//2 - 1]]
    direction = curses.KEY_RIGHT

    for y, x in snake:
        stdscr.addch(y, x, '#')

    food = create_food(snake, box)
    stdscr.addch(food[0], food[1], '*')

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
            food = create_food(snake, box)
            stdscr.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1]  in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]):
            break

        stdscr.addch(snake[0][0], snake[0][1], '#')

curses.wrapper(main)
import random
import curses

def create_food(snake, box):
    food = None
    while food is None:
        food = [random.randint(box[0][0]+1, box[1][0]-1), random.randint(box[0][1]+1, box[1][1]-1)]
        if food in snake:
            food is None
    return food

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3, sw-3]]
    stdscr.box()

    snake = [[sh//2, sw//2 + 1], [sh//2, sw//2], [sh//2, sw//2 - 1]]
    direction = curses.KEY_RIGHT

    for y, x in snake:
        stdscr.addch(y, x, '#')

    food = create_food(snake, box)
    stdscr.addch(food[0], food[1], '*')

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
            food = create_food(snake, box)
            stdscr.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1] in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]):
            break

        stdscr.addch(snake[0][0], snake[0][1], '#')

curses.wrapper(main)
