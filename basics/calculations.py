#!/usr/bin/env python3

"""
This module is about calculation.

Classes
    -------------
    BasicCalculation
"""


class BasicCalculation:
    """
    This class does simple magic with numbers

    Note:
        adds two numbers.

    Attributes:
        none:

    """

    def add(self, number1, number2):
        """
        This method adds two numbers to each other

        Args:
            number1 : integer
                first input for calc.
            number2 : integer
                second input for calc.
        Returns:
            integer: result of addition
        Raises:
            none

        """
        return number1 + number2

    def substract(self, number1, number2):
        return number1 - number2

    def devide(self, number1, number2):
        return number1 / number2

    def multiply(self, number1, number2):
        return number1 * number2
