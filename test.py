import unittest
import argparse
from game import main, COLORS 

class TestArgParse(unittest.TestCase):

    def test_defaults(self):
        # Simulate running: python game.py Play
        args = main().parse_args(["Play"])
        self.assertEqual(args.width, 800)
        self.assertEqual(args.height, 600)
        self.assertEqual(args.player_speed, 5)
        self.assertEqual(args.player_color, "PURPLE")

    def test_custom_values(self):
        # Simulate running: python game.py Play --width 1024 --height 768 --player_speed 10 --player_color BLUE
        args = main().parse_args(["Play", "--width", "1024", "--height", "768", "--player_speed", "10", "--player_color", "BLUE"])
        self.assertEqual(args.width, 1024)
        self.assertEqual(args.height, 768)
        self.assertEqual(args.player_speed, 10)
        self.assertEqual(args.player_color, "BLUE")

    def test_invalid_color(self):
        # Simulate running with an invalid color
        with self.assertRaises(SystemExit):  # argparse exits on invalid input
            main().parse_args(["Play", "--player_color", "ORANGE"])

if __name__ == "__main__":
    unittest.main()
