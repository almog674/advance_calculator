"""
Name: parenthesis_handler.py
Author: Almog Maimon
Purpose:
Date: 01/10/2022
"""
from typing import Tuple

from parenthesis_handler.abstract_parenthesis_handler import AbstractParenthesisHandler, InvalidParenthesis
from parenthesis_handler.parenthesis_validator import ParenthesisValidator


class ParenthesisHandler(AbstractParenthesisHandler):
    """
    Handles the parenthesis in an equation.
    """

    def __init__(self, parenthesis_validator: ParenthesisValidator):
        super(ParenthesisHandler, self).__init__(parenthesis_validator)

    @staticmethod
    def _get_equation_inside_parenthesis(equation: str) -> Tuple[str, str]:
        first_index = equation.rfind('(')
        new_eq = equation[first_index::]
        second_index = first_index + new_eq.index(')')

        equation_without_parenthesis = equation[first_index +
                                       1:second_index]
        equation_with_parenthesis = equation[first_index:second_index + 1]

        return equation_without_parenthesis, equation_with_parenthesis

    def handle_parenthesis(self, equation: str) -> Tuple[bool, str, str]:
        if not self.parenthesis_validator.is_parenthesis_valid(equation):
           raise InvalidParenthesis(f"There is invalid parenthesis in {equation}")

        if '(' in equation:
            equation_without_parenthesis, equation_with_parenthesis = self._get_equation_inside_parenthesis(equation)

            return True, equation_with_parenthesis, equation_without_parenthesis
        else:
            return False, "", ""
