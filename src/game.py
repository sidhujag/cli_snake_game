class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.direction = 'UP'
        self.score = 0
        self.food = None
        self.place_food()

    def place_food(self):
        import random
        while True:
            self.food = (random.randint(1, self.width - 2), random.randint(1, self.height - 2))
            if self.food not in self.snake:
                break

    def change_direction(self, new_direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.update_score()
            self.place_food()
        else:
            self.snake.pop()

    def check_collision(self):
        head_x, head_y = self.snake[0]
        return (
            head_x in (0, self.width - 1) or
            head_y in (0, self.height - 1) or
            self.snake[0] in self.snake[1:]
        )

    def update_score(self):
        self.score += 1

    def run(self):
        # Main game loop
        pass
