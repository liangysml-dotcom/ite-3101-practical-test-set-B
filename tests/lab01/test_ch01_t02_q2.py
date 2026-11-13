import sys
import unittest
from unittest.mock import patch

from lab.lab01.ch01_t02_q2 import main
from tests.unit_test_helper.console_test_helper import MyOutput


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.my_stdout = MyOutput()
        self.original_stdout = sys.stdout
        sys.stdout = self.my_stdout

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_2d3_3d4_4d5(self):
        user_input = ['2.3', '3.4', "4.5"]

        with patch('builtins.input', side_effect=user_input):
            main()
        self.assertEqual("The volume of a Pyramid is 11.73.\n", str(self.my_stdout))

    def test_1_1_1(self):
        user_input = ['1', '1', "1"]

        with patch('builtins.input', side_effect=user_input):
            main()
        self.assertEqual("The volume of a Pyramid is 0.33.\n", str(self.my_stdout))


    def test_float(self):
        user_input = ['1.5', '1.5', "1.5"]

        with patch('builtins.input', side_effect=user_input):
            main()
        self.assertEqual("The volume of a Pyramid is 1.12.\n", str(self.my_stdout))

    def test_a_2_3(self):
        user_input = ['a', '2', "3"]

        with self.assertRaises(SystemExit) as cm:
            with patch('builtins.input', side_effect=user_input):
                main()
        self.assertEqual(-1, cm.exception.code)
        self.assertEqual("Invalid input!\n", str(self.my_stdout))

    def test_1_a_3(self):
        user_input = ['1', 'a', "3"]

        with self.assertRaises(SystemExit) as cm:
            with patch('builtins.input', side_effect=user_input):
                main()
        self.assertEqual(-1, cm.exception.code)
        self.assertEqual("Invalid input!\n", str(self.my_stdout))

    def test_1_2_a(self):
        user_input = ['1', '2', "a"]

        with self.assertRaises(SystemExit) as cm:
            with patch('builtins.input', side_effect=user_input):
                main()
        self.assertEqual(-1, cm.exception.code)
        self.assertEqual("Invalid input!\n", str(self.my_stdout))


if __name__ == '__main__':
    unittest.main()
