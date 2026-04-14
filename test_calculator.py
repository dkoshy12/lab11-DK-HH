#https://github.com/dkoshy12/lab11-DK-HH
#Partner 1: Daniel Koshy
#Partner 2: Haseeb Haq

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = calculator.add(3, 5)
        self.assertEqual(result, 8)

        result = calculator.add(-1, 1)
        self.assertEqual(result, 0)

        result = calculator.add(0, 0)
        self.assertEqual(result, 0)

    def test_subtract(self):
        result = calculator.subtract(10, 4)
        self.assertEqual(result, 6)

        result = calculator.subtract(5, 0)
        self.assertEqual(result, 5)

        result = calculator.subtract(-3, -3)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = calculator.mul(3, 4)
        self.assertEqual(result, 12)

        result = calculator.mul(-2, 5)
        self.assertEqual(result, -10)

        result = calculator.mul(0, 100)
        self.assertEqual(result, 0)

    def test_divide(self):
        result = calculator.div(2, 10)
        self.assertEqual(result, 5)

        result = calculator.div(4, 1)
        self.assertAlmostEqual(result, 0.25)

        result = calculator.div(-2, 8)
        self.assertEqual(result, -4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        result = calculator.logarithm(10, 100)
        self.assertAlmostEqual(result, 2.0)

        result = calculator.logarithm(2, 8)
        self.assertAlmostEqual(result, 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)

        with self.assertRaises(ValueError):
            calculator.logarithm(10, -5)

    def test_hypotenuse(self):
        result = calculator.hypotenuse(3, 4)
        self.assertAlmostEqual(result, 5.0)

        result = calculator.hypotenuse(0, 5)
        self.assertAlmostEqual(result, 5.0)

        result = calculator.hypotenuse(-3, 4)
        self.assertAlmostEqual(result, 5.0)

    def test_sqrt(self):
        result = calculator.square_root(9)
        self.assertAlmostEqual(result, 3.0)

        result = calculator.square_root(0)
        self.assertAlmostEqual(result, 0.0)

        with self.assertRaises(ValueError):
            calculator.square_root(-1)


if __name__ == "__main__":
    unittest.main()
