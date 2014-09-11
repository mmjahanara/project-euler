import unittest

from util import Fraction

class FractionTest(unittest.TestCase):
    def testAdd(self):
        a = Fraction(15, 12)
        b = Fraction(2, 5)
        c = a + b
        self.assertEqual(20, c.denominator)
        self.assertEqual(33, c.numerator)
    def testMul(self):
        a = Fraction(15, 12)
        b = Fraction(2, 5)
        c = a * b
        self.assertEqual(2, c.denominator)
        self.assertEqual(1, c.numerator)
    def testDiv(self):
        a = Fraction(1)
        b = Fraction(2, 5)
        c = a / b
        self.assertEqual(2, c.denominator)
        self.assertEqual(5, c.numerator)

if __name__ == '__main__':
    unittest.main()
