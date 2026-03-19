import unittest
from logic import CalculatorLogic


class TestCalculatorLogic(unittest.TestCase):
    def setUp(self):
        self.logic = CalculatorLogic()

    def test_basic_arithmetic(self):
        self.assertEqual(self.logic.evaluate("2+3"), "5")
        self.assertEqual(self.logic.evaluate("10-4"), "6")
        self.assertEqual(self.logic.evaluate("6*7"), "42")
        self.assertEqual(self.logic.evaluate("20/5"), "4")

    def test_decimal_inputs(self):
        self.assertEqual(self.logic.evaluate("1.5+2.5"), "4")
        self.assertEqual(self.logic.evaluate("10.5-0.5"), "10")
        self.assertEqual(self.logic.evaluate("2.5*4"), "10")
        self.assertEqual(self.logic.evaluate("7.5/2.5"), "3")

    def test_division_by_zero(self):
        self.assertEqual(self.logic.evaluate("1/0"), "Error")

    def test_syntax_error(self):
        self.assertEqual(self.logic.evaluate("2++2"), "Error")
        self.assertEqual(self.logic.evaluate("invalid"), "Error")

    def test_allowed_chars(self):
        self.assertEqual(self.logic.evaluate("2+2!"), "Error")
        self.assertEqual(self.logic.evaluate("import os"), "Error")

    def test_float_formatting(self):
        # Should return 4 instead of 4.0
        self.assertEqual(self.logic.evaluate("8/2"), "4")
        # Should retain decimal if non-integer
        self.assertEqual(self.logic.evaluate("1/2"), "0.5")


if __name__ == "__main__":
    unittest.main()
