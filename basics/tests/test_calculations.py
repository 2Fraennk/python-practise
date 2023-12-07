#!/usr/bin/env python3

import basics.calculations as calculation
import unittest


class TestCalculation(unittest.TestCase):
    def test_add(self):
        result = calculation.BasicCalculation.add(self, 1, 2)
        print("calculated result is: ", result)
        assert result >= 3
        # pass   #this lets the test pass
    def test_substrac(self):
        result = calculation.BasicCalculation.substract(self, 1, 2)
        print("calculated result is: ", result)
        assert result <= 0
        # pass   #this lets the test pass
    def test_devide(self):
        result = calculation.BasicCalculation.devide(self, 1, 2)
        print("calculated result is: ", result)
        assert result == 0.5
        # pass   #this lets the test pass
    def test_multiply(self):
        result = calculation.BasicCalculation.multiply(self, 1, 2)
        print("calculated result is: ", result)
        assert result == 2
        # pass   #this lets the test pass

if __name__ == "__main__":
    unittest.main()
