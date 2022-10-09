"""
Name: sunequation_finder.py
Author: Almog Maimon
Purpose:
Date: 01/10/2022
"""
from typing import Tuple, List

from custom_operator import Operator
from operators_manager.base_operators_manager import BaseOperatorsManager
from parenthesis_handler.abstract_parenthesis_handler import AbstractParenthesisHandler


class SubequationFinder:
    def __init__(self, operators_manager: BaseOperatorsManager, parenthesis_handler: AbstractParenthesisHandler,
                 special_characters: List[str]):
        self.operators_manager = operators_manager
        self.special_characters = special_characters
        self.parenthesis_handler = parenthesis_handler

    def get_subequation(self, equation: str):
        there_are_parenthesis, equation_with_parenthesis, equation_without_parenthesis = \
            self.parenthesis_handler.handle_parenthesis(equation)

        if there_are_parenthesis:
            operator, subequation = self.get_subequation_with_parenthesis(equation_with_parenthesis)
        else:
            operator, subequation = self.get_subequation_no_parenthesis(equation)

        return subequation, operator

    def get_subequation_with_parenthesis(self, equation_with_parenthesis: str) -> Tuple[Operator, str]:
        subequation = equation_with_parenthesis
        operator_index, operator = self.operators_manager.get_equation_strongest_operator(subequation)
        return operator, subequation

    def get_subequation_no_parenthesis(self, equation: str) -> Tuple[Operator, str]:
        operator_index, operator = self.operators_manager.get_equation_strongest_operator(equation)

        if operator.type == "unery":
            subequation = self._get_unery_subequation(equation, operator_index)
        else:
            subequation = self._get_binary_subequation(equation, operator_index)

        return operator, subequation

    def is_statement_solved(self, equation: str) -> bool:
        return not self.operators_manager.get_equation_strongest_operator(equation)[0]

    def _get_start_index(self, equation, operator_index):
        start_index = operator_index - 1
        char = equation[start_index]

        while True:
            if not (char.isnumeric() or char in self.special_characters):
                start_index += 2
                break

            elif start_index == 0:
                break

            else:
                char = equation[start_index]
            start_index -= 1

        return start_index

    def _get_end_index(self, equation, operator_index):
        end_index = operator_index + 1
        char = equation[end_index]

        while True:
            if not (char.isnumeric() or char in self.special_characters):
                end_index -= 1
                break

            elif end_index > len(equation) - 1:
                end_index += 1
                break

            else:
                char = equation[end_index]
            end_index += 1

        return end_index

    def _get_binary_subequation(self, equation: str, operator_index: int) -> str:
        start_index = self._get_start_index(equation, operator_index)
        end_index = self._get_end_index(equation, operator_index)

        sub_statement = equation[start_index:end_index]

        return sub_statement

    def _get_unery_subequation(self, equation: str, operator_index: int) -> str:
        end_index = self._get_end_index(equation, operator_index)
        sub_statement = equation[operator_index:end_index]

        return sub_statement
