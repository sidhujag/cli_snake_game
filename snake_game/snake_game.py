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
