import unittest
from unittest.mock import patch
from snake_game import create_food

class TestCreateFood(unittest.TestCase):
    def test_create_food_not_in_snake(self):
        snake = [[5, 5], [5, 4], [5, 3]]
        box = [[1, 1], [10, 10]]
        with patch('snake_game.random.randint', side_effect=[6, 6]):
            food = create_food(snake, box)
            self.assertNotIn(food, snake)
            self.assertTrue(box[0][0] < food[0] < box[1][0])
            self.assertTrue(box[0][1] < food[1] < box[1][1])

    def test_create_food_retries_when_in_snake(self):
        snake = [[5, 5], [5, 4], [5, 3]]
        box = [[1, 1], [10, 10]]
        with patch('snake_game.random.randint', side_effect=[5, 5, 6, 6]):
            food = create_food(snake, box)
            self.assertEqual(food, [6, 6])

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from snake_game import create_food, GameState, update_game_state, handle_keypress

class TestSnakeGame(unittest.TestCase):
    def test_create_food_not_in_snake(self):
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        with patch('snake_game.random.randint', side_effect=[6, 6]):
            food = create_food(snake, box)
            self.assertNotIn(food, snake)
            self.assertTrue(box[0][0] < food[0] < box[1][0])
            self.assertTrue(box[0][1] < food[1] < box[1][1])

    def test_game_loop_logic(self):
        state = GameState()
        state.snake = [(5, 5), (5, 4), (5, 3)]
        state.food = (6, 6)
        with patch('snake_game.get_keypress', return_value='d'):
            handle_keypress(state, 'd')
            self.assertEqual(state.direction.name, 'RIGHT')
            update_game_state(state)
            self.assertEqual(state.snake[0], (6, 5))
            self.assertFalse(state.game_over)

if __name__ == '__main__':
    unittest.main()
