import unittest
from arithmetic import *

class ArithmeticTest(unittest.TestCase): # <1>

    def test_multiplication(self): # <2>
        self.assertEqual(multiply(2, 2), 4)

    def test_divsion(self):
        self.assertEqual(divide(10, 3), 3.3333333333333333)

if __name__ == '__main__':
    unittest.main()
