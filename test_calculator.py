import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-5, 2), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-1, 2), -3)
        self.assertEqual(self.calc.subtract(-5, 2), -7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 2), 20)
        self.assertEqual(self.calc.multiply(5, -2), -10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(15,5),3)
        self.assertEqual(self.calc.divide(10, 3), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(15,5),0)
        self.assertEqual(self.calc.modulo(10, 3), 1)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()