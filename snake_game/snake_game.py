import random
import curses

def create_food(snake, box):
    food = None
    while food is None:
        food = [random.randint(box[0][0]+1, box[1][0]-1), random.randint(box[0][1]+1, box[1][1]-1)]
        if food in snake:
            food = None
    return food

def initialize_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3, sw-3]]
    snake = [[sh//2, sw//2 + 1], [sh//2, sw//2], [sh//2, sw//2 - 1]]
    direction = curses.KEY_RIGHT
    food = create_food(snake, box)
    score = 0
    return {'stdscr': stdscr, 'box': box, 'snake': snake, 'direction': direction, 'food': food, 'score': score, 'game_over': False}

def render_score(stdscr, score):
    score_text = 'Score: {}'.format(score)
    stdscr.addstr(1, 2, score_text)

def game_loop(game_state):
    while not game_state['game_over']:
        stdscr = game_state['stdscr']
        stdscr.clear()
        render_score(stdscr, game_state['score'])
        next_key = stdscr.getch()
        handle_input(game_state, next_key)
        update_snake_position(game_state)
        check_collisions(game_state)
        update_food(game_state)
        render_game_state(game_state)
        stdscr.refresh()
        if game_state['game_over']:
            handle_game_over(stdscr)

def handle_input(game_state, key):
    key_to_direction = {
        curses.KEY_UP: 'UP',
        curses.KEY_DOWN: 'DOWN',
        curses.KEY_LEFT: 'LEFT',
        curses.KEY_RIGHT: 'RIGHT',
    }
    if key in key_to_direction:
        current_direction = game_state['direction']
        new_direction = key_to_direction[key]
        # Prevent the snake from reversing on itself
        if (current_direction == 'UP' and new_direction != 'DOWN') or \
           (current_direction == 'DOWN' and new_direction != 'UP') or \
           (current_direction == 'LEFT' and new_direction != 'RIGHT') or \
           (current_direction == 'RIGHT' and new_direction != 'LEFT'):
            game_state['direction'] = new_direction

def update_snake_position(game_state):
    head = game_state['snake'][0]
    dx, dy = game_state['directions'][game_state['direction']]
    new_head = (head[0] + dy, head[1] + dx)
    game_state['snake'].insert(0, new_head)
    if new_head == game_state['food']:
        game_state['food'] = create_food(game_state['snake'], game_state['box'])
    else:
        game_state['snake'].pop()

def check_collisions(game_state):
    head = game_state['snake'][0]
    if head in game_state['snake'][1:] or \
       head[0] <= game_state['box'][0][0] or head[0] >= game_state['box'][1][0] or \
       head[1] <= game_state['box'][0][1] or head[1] >= game_state['box'][1][1]:
        game_state['game_over'] = True

def update_food(game_state):
    if game_state['snake'][0] == game_state['food']:
        game_state['food'] = create_food(game_state['snake'], game_state['box'])
        game_state['score'] += 1

def render_game_state(game_state):
    stdscr = game_state['stdscr']
    stdscr.clear()
    stdscr.border(0)
    for y, x in game_state['snake']:
        stdscr.addch(y, x, '#')
    stdscr.addch(game_state['food'][0], game_state['food'][1], '*')
    stdscr.refresh()

def handle_game_over(stdscr, score):
    stdscr.clear()
    sh, sw = stdscr.getmaxyx()
    msg = "Game Over! Your score was: {}".format(score)
    stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
    stdscr.refresh()
    stdscr.nodelay(0)
    stdscr.getch()

def main(stdscr):
    game_state = initialize_game(stdscr)
    game_loop(game_state)

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

def update_food(game_state):
    if game_state['snake'][0] == game_state['food']:
        game_state['food'] = create_food(game_state['snake'], game_state['box'])
        game_state['score'] += 1

def render_game_state(game_state):
    stdscr = game_state['stdscr']
    stdscr.clear()
    stdscr.border(0)
    for y, x in game_state['snake']:
        stdscr.addch(y, x, '#')
    stdscr.addch(game_state['food'][0], game_state['food'][1], '*')
    stdscr.refresh()

def handle_game_over(stdscr, score):
    stdscr.clear()
    sh, sw = stdscr.getmaxyx()
    msg = "Game Over! Your score was: {}".format(score)
    stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
    stdscr.refresh()
    stdscr.nodelay(0)
    stdscr.getch()

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
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    snake = [[sh//2, sw//2 + 1], [sh//2, sw//2], [sh//2, sw//2 - 1]]
    direction = curses.KEY_RIGHT

    for y, x in snake:
        stdscr.addstr(y, x, '#')

    food = create_food(snake, box)
    stdscr.addstr(food[0], food[1], '*')

    score = 0
    while True:
        key = stdscr.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        head = [snake[0][0], snake[0][1]]

        if direction == curses.KEY_RIGHT:
            head[1] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1

        snake.insert(0, head)

        if snake[0] == food:
            score += 1
            food = create_food(snake, box)
            stdscr.addstr(food[0], food[1], '*')
        else:
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1]  in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]):
            msg = "Game Over!"
            stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
            stdscr.nodelay(0)
            stdscr.getch()
            break

        stdscr.addstr(snake[0][0], snake[0][1], '#')

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
