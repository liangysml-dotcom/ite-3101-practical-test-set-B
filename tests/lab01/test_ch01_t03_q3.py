import sys
import unittest
from unittest.mock import patch

from lab.lab01.ch01_t03_q3 import main, get_number_sequence
from tests.unit_test_helper.console_test_helper import MyOutput


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.my_stdout = MyOutput()
        self.original_stdout = sys.stdout
        sys.stdout = self.my_stdout

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_get_number_sequence_3_and_6(self):
        result = get_number_sequence(3)
        self.assertEqual("321", result)
        result = get_number_sequence(6)
        self.assertEqual("654321", result)

    def test_get_number_sequence_negative_1(self):
        result = get_number_sequence(-1)
        self.assertEqual("", result)

    def test_3_and_6(self):
        user_input = ['3']
        with patch('builtins.input', side_effect=user_input):
            main()
        expected = '''1
21
321
'''
        self.assertEqual(expected, str(self.my_stdout))

        user_input = ['6']
        with patch('builtins.input', side_effect=user_input):
            main()
        expected = '''1
21
321
1
21
321
4321
54321
654321
'''
        self.assertEqual(expected, str(self.my_stdout))

    def test_negative_1(self):
        user_input = ['-1']
        with self.assertRaises(SystemExit) as cm:
            with patch('builtins.input', side_effect=user_input):
                main()
        self.assertEqual(-1, cm.exception.code)
        self.assertEqual("You must enter a positive integer.\n", str(self.my_stdout))

    def test_invalid_a(self):
        user_input = ['a']
        with self.assertRaises(SystemExit) as cm:
            with patch('builtins.input', side_effect=user_input):
                main()
        self.assertEqual(-1, cm.exception.code)
        self.assertEqual("You must enter an integer.\n", str(self.my_stdout))


if __name__ == '__main__':
    unittest.main()
