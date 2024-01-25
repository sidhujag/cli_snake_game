class Renderer:
    def __init__(self, game):
        self.game = game

    def render(self):
        self.clear_screen()
        for y in range(self.game.height):
            for x in range(self.game.width):
                if (x, y) == self.game.snake[0]:
                    print('O', end='')
                elif (x, y) in self.game.snake:
                    print('o', end='')
                elif (x, y) == self.game.food:
                    print('X', end='')
                else:
                    print(' ' if x not in (0, self.game.width - 1) and y not in (0, self.game.height - 1) else '#', end='')
            print()

    def display_score(self):
        print(f'Score: {self.game.score}')

    def clear_screen(self):
        print('\033[H\033[J', end='')

    def game_over(self):
        print('Game Over!')
        print(f'Final Score: {self.game.score}')
        print('Press any key to exit...')
