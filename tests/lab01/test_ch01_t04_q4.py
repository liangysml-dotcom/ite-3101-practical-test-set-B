import itertools
import sys
import unittest
from unittest.mock import patch

from lab.lab01.ch01_t04_q4 import main, check_prime_num
from tests.unit_test_helper.console_test_helper import MyOutput


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.my_stdout = MyOutput()
        self.original_stdout = sys.stdout
        sys.stdout = self.my_stdout

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_check_prime_num_2_false(self):        
        self.assertTrue(check_prime_num(2))

    def test_check_prime_num_false(self):
        for n in range(4, 100, 2):
            self.assertFalse(check_prime_num(n))

    def test_check_prime_num_true(self):
        tests = [ 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for n in tests:
            self.assertTrue(check_prime_num(n))       

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

    def test_true(self):
        user_input = ['3']     
        with patch('builtins.input', side_effect=user_input):
            main()        
        self.assertEqual("3 is a Prime number\n", str(self.my_stdout))

    def test_false(self):
        user_input = ['100']     
        with patch('builtins.input', side_effect=user_input):
            main()        
        self.assertEqual("100 is not a Prime number\n", str(self.my_stdout))        

if __name__ == '__main__':
    unittest.main()
