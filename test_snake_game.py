import unittest
from unittest.mock import patch
from snake_game import create_food

class TestCreateFoodFunction(unittest.TestCase):
    def test_create_food_not_on_snake(self):
        """Test food is created not on the snake."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        # Run the test multiple times to check random behavior
        for _ in range(100):
            food = create_food(snake, box)
            self.assertNotIn(food, snake, "The food should not be placed on the snake's body.")

    def test_create_food_within_boundaries(self):
        """Test food is created within the box boundaries."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        # Run the test multiple times to check random behavior
        for _ in range(100):
            food = create_food(snake, box)
            self.assertTrue(box[0][0] < food[0] < box[1][0], "Food's x-coordinate is out of horizontal boundaries.")
            self.assertTrue(box[0][1] < food[1] < box[1][1], "Food's y-coordinate is out of vertical boundaries.")

    def test_create_food_unique_location(self):
        """Test food is created at a unique location each time."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        food_locations = set()
        # Run the test multiple times to check for unique food placement
        for _ in range(20):
            food = create_food(snake, box)
            self.assertNotIn(food, food_locations, "The food should be placed at a new location each time.")
            food_locations.add(food)
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
from snake_game import create_food

class TestCreateFoodFunction(unittest.TestCase):
    def test_create_food_not_on_snake(self):
        """Test food is created not on the snake."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        # Run the test multiple times to check random behavior
        for _ in range(100):
            food = create_food(snake, box)
            self.assertNotIn(food, snake, "The food should not be placed on the snake's body.")

    def test_create_food_within_boundaries(self):
        """Test food is created within the box boundaries."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        # Run the test multiple times to check random behavior
        for _ in range(100):
            food = create_food(snake, box)
            self.assertTrue(box[0][0] < food[0] < box[1][0], "Food's x-coordinate is out of horizontal boundaries.")
            self.assertTrue(box[0][1] < food[1] < box[1][1], "Food's y-coordinate is out of vertical boundaries.")

    def test_create_food_unique_location(self):
        """Test food is created at a unique location each time."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        food_locations = set()
        # Run the test multiple times to check for unique food placement
        for _ in range(20):
            food = create_food(snake, box)
            self.assertNotIn(food, food_locations, "The food should be placed at a new location each time.")
            food_locations.add(food)
from snake_game import create_food, GameState, update_game_state, handle_keypress

class TestSnakeGame(unittest.TestCase):
    def test_create_food_not_on_snake_body(self):
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        for _ in range(100):  # Run the test multiple times to check random behavior
            food = create_food(snake, box)
            self.assertNotIn(food, snake, "The food should not be placed on the snake's body.")

    def test_create_food_within_boundaries(self):
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        for _ in range(100):  # Run the test multiple times to check random behavior
            food = create_food(snake, box)
            self.assertTrue(box[0][0] <= food[0] <= box[1][0], "Food's x-coordinate is out of horizontal boundaries.")
            self.assertTrue(box[0][1] <= food[1] <= box[1][1], "Food's y-coordinate is out of vertical boundaries.")

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
import unittest
from unittest.mock import patch
from snake_game import create_food

class TestCreateFoodFunction(unittest.TestCase):
    def test_create_food_not_on_snake(self):
        """Test food is created not on the snake."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        # Run the test multiple times to check random behavior
        for _ in range(100):
            food = create_food(snake, box)
            self.assertNotIn(food, snake, "The food should not be placed on the snake's body.")

    def test_create_food_within_boundaries(self):
        """Test food is created within the box boundaries."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        # Run the test multiple times to check random behavior
        for _ in range(100):
            food = create_food(snake, box)
            self.assertTrue(box[0][0] < food[0] < box[1][0], "Food's x-coordinate is out of horizontal boundaries.")
            self.assertTrue(box[0][1] < food[1] < box[1][1], "Food's y-coordinate is out of vertical boundaries.")

    def test_create_food_unique_location(self):
        """Test food is created at a unique location each time."""
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        food_locations = set()
        # Run the test multiple times to check for unique food placement
        for _ in range(20):
            food = create_food(snake, box)
            self.assertNotIn(food, food_locations, "The food should be placed at a new location each time.")
            food_locations.add(food)
from snake_game import create_food

class TestCreateFood(unittest.TestCase):
    def test_create_food_not_in_snake(self):
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        with patch('snake_game.random.randint', side_effect=[6, 6]):
            food = create_food(snake, box)
            self.assertNotIn(food, snake, "The food should not be placed on the snake's body.")

    def test_create_food_within_boundaries(self):
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        with patch('snake_game.random.randint', side_effect=[6, 6]):
            food = create_food(snake, box)
            self.assertTrue(box[0][0] <= food[0] <= box[1][0], "Food's x-coordinate is out of horizontal boundaries.")
            self.assertTrue(box[0][1] <= food[1] <= box[1][1], "Food's y-coordinate is out of vertical boundaries.")

    def test_create_food_retries_when_in_snake(self):
        snake = [(5, 5), (5, 4), (5, 3)]
        box = [(1, 1), (10, 10)]
        with patch('snake_game.random.randint', side_effect=[5, 5, 6, 6]):
            food = create_food(snake, box)
            self.assertEqual(food, [6, 6], "The food should be placed at a new location if the first is occupied by the snake.")

if __name__ == '__main__':
    unittest.main()
