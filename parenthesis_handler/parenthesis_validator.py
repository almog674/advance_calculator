"""
Name: parenthesis_validator.py
Author: Almog Maimon
Purpose: Making sure that an equation have valid parenthesis.
Date: 01/10/2022
"""


class ParenthesisValidator:
    @staticmethod
    def is_parenthesis_valid(equation: str) -> bool:
        parenthesis_counter = 0

        for letter in equation:
            if letter == ")":
                parenthesis_counter -= 1
            elif letter == "(":
                parenthesis_counter += 1

            if parenthesis_counter < 0:
                return False

        return parenthesis_counter == 0
