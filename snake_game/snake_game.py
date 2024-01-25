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
    # Initialization
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3, sw-3]]
    snake = [[sh//2, sw//2 + 1], [sh//2, sw//2], [sh//2, sw//2 - 1]]
    direction = curses.KEY_RIGHT

    for y, x in box:
        stdscr.addch(y, x, '+')

    food = create_food(snake, box)  # Initial food placement
    # Draw game border
    for y in range(box[0][0], box[1][0]):
        for x in range(box[0][1], box[1][1]):
            if y in [box[0][0], box[1][0]-1] or x in [box[0][1], box[1][1]-1]:
                stdscr.addch(y, x, '+')

    # Initial food placement
    food = create_food(snake, box)
    stdscr.addch(food[0], food[1], '#')

    score = 0

    # Game loop
    while True:
        # Input handling
    while True:
        next_key = stdscr.getch()
        direction = direction if next_key == -1 else next_key

        # Snake movement
        head = [snake[0][0], snake[0][1]]

        # Direction handling
        if direction == curses.KEY_DOWN:
            head[0] += 1
        if direction == curses.KEY_UP:
            head[0] -= 1
        if direction == curses.KEY_LEFT:
            head[1] -= 1
        if direction == curses.KEY_RIGHT:
            head[1] += 1

        # Insert new head
        snake.insert(0, head)

        # Food consumption
        if snake[0] == food:
            score += 1
            food = create_food(snake, box)
            food = create_food(snake, box)  # Place new food
            stdscr.addch(food[0], food[1], '#')
        else:
            # Move snake
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1]  in [box[0][1], box[1][1]] or
        # Collision detection
        if (snake[0][0] in [box[0][0], box[1][0]-1] or
            snake[0][1]  in [box[0][1], box[1][1]-1] or
            snake[0] in snake[1:]):
            break

        # Render snake
        stdscr.addch(snake[0][0], snake[0][1], '*')

    # Game over message
    stdscr.addstr(sh//2, sw//2 - len("Game Over!")//2, "Game Over!")
    stdscr.nodelay(0)
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
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
    # Initialization
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

        # Snake movement
        head = [snake[0][0], snake[0][1]]

        # Direction handling
        if direction == curses.KEY_DOWN:
            head[0] += 1
        if direction == curses.KEY_UP:
            head[0] -= 1
        if direction == curses.KEY_LEFT:
            head[1] -= 1
        if direction == curses.KEY_RIGHT:
            head[1] += 1

        # Insert new head
        snake.insert(0, head)

        if snake[0] == food:
            food = create_food(snake, box)
            stdscr.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1]  in [box[0][1], box[1][1]] or
        # Collision detection
        if (snake[0][0] in [box[0][0], box[1][0]-1] or
            snake[0][1]  in [box[0][1], box[1][1]-1] or
            snake[0] in snake[1:]):
            break

        stdscr.addch(snake[0][0], snake[0][1], '#')

curses.wrapper(main)
