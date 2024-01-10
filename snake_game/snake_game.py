import random
import curses
from collections import deque

class SnakeGame:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.window = curses.newwin(height, width, 0, 0)
        self.window.keypad(1)
        self.window.timeout(100)
        self.snake = deque([(height//2, width//4)])
        self.snake_dir = curses.KEY_RIGHT
        self.food = self.spawn_food()
        self.score = 0

    def spawn_food(self):
        food = None
        while food is None:
            food = (random.randint(1, self.height-2), random.randint(1, self.width-2))
            if food in self.snake:
                food = None
        return food

    def render(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 2, 'Score : ' + str(self.score) + ' ')
        self.window.addch(self.food[0], self.food[1], '*')
        for idx, part in enumerate(self.snake):
            if idx == 0:
                self.window.addch(part[0], part[1], '@')
            else:
                self.window.addch(part[0], part[1], '#')
        self.window.refresh()

    def update(self):
        next_key = self.window.getch()
        if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            self.snake_dir = next_key

        head = self.snake[0]
        if self.snake_dir == curses.KEY_RIGHT:
            new_head = (head[0], head[1]+1)
        elif self.snake_dir == curses.KEY_LEFT:
            new_head = (head[0], head[1]-1)
        elif self.snake_dir == curses.KEY_UP:
            new_head = (head[0]-1, head[1])
        elif self.snake_dir == curses.KEY_DOWN:
            new_head = (head[0]+1, head[1])

        self.snake.appendleft(new_head)
        if self.snake[0] == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        if (self.snake[0][0] in [0, self.height-1] or
            self.snake[0][1]  in [0, self.width-1] or
            self.snake[0] in list(self.snake)[1:]):
            raise Exception("Game Over")

def main(stdscr):
    curses.curs_set(0)
    game = SnakeGame()
    while True:
        game.render()
        try:
            game.update()
        except Exception as e:
            stdscr.addstr(game.height//2, game.width//2 - len(str(e))//2, str(e))
            stdscr.refresh()
            stdscr.getch()
            break

if __name__ == "__main__":
    curses.wrapper(main)
