import sys
import unittest
from unittest.mock import patch
from tests.unit_test_helper.console_test_helper import MyOutput
from lab.lab01.ch01_t01_q1 import main

class TestOutput(unittest.TestCase):
    def setUp(self):
        self.my_stdout = MyOutput()
        self.original_stdout = sys.stdout
        sys.stdout = self.my_stdout

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_3(self):
        user_input = [
            '3'
        ]

        with patch('builtins.input', side_effect=user_input):
            main()

        self.assertEqual("3 is not divisible by both 2 or 9.\n", str(self.my_stdout))

    def test_5(self):
        user_input = [
            '5'
        ]

        with patch('builtins.input', side_effect=user_input):
            main()

        self.assertEqual("5 is not divisible by both 2 or 9.\n", str(self.my_stdout))

    def test_16(self):
        user_input = [
            '16'
        ]

        with patch('builtins.input', side_effect=user_input):
            main()

        self.assertEqual("16 is divisible by both 2 or 9.\n", str(self.my_stdout))

    def test_a_b_d_16(self):
        user_input = [
            'a',
            'b',
            'c',
            '16'
        ]

        with patch('builtins.input', side_effect=user_input):
            main()

        expected = '''Please enter an integer.
Please enter an integer.
Please enter an integer.
16 is divisible by both 2 or 9.
'''

        self.assertEqual(expected, str(self.my_stdout))

    def test_a_b_d_17(self):
        user_input = [
            'a',
            'b',
            'c',
            '17'
        ]

        with patch('builtins.input', side_effect=user_input):
            main()

        expected = '''Please enter an integer.
Please enter an integer.
Please enter an integer.
17 is not divisible by both 2 or 9.
'''

        self.assertEqual(expected, str(self.my_stdout))


if __name__ == '__main__':
    unittest.main()
