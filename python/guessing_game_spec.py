from guessing_game import GuessingGame
from unittest import TestCase, main

class GuessingGameTestCase(TestCase):
    """ tests for the guessinggame class"""
    def setUp(self):
        self.guessing_game = GuessingGame(5)

    def test_guess_10_returns_high(self):
        self.assertEqual(self.guessing_game.guess(10), 'high')

    def test_guess_1_returns_low(self):
        self.assertEqual(self.guessing_game.guess(1), 'low')

    def test_guess_5_returns_correct(self):
        self.assertEqual(self.guessing_game.guess(5), 'correct')
        self.assertEqual(self.guessing_game.solved, True)
    

if __name__ == "__main__":
    main()