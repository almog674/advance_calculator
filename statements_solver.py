"""
Name: statements_solver.py
Author: Almog Maimon
Purpose:
Date: 01/10/2022
"""
from typing import Tuple

from operators_manager.custom_operator import Operator
from number_formatter.base_number_formatter import BaseNumberFormatter
from sunequation_finder import SubequationFinder


class StatementsSolver:
    def __init__(self, subequation_finder: SubequationFinder, number_formatter: BaseNumberFormatter):
        self.subequation_finder = subequation_finder
        self.number_formatter = number_formatter

    def solve_statement(self, statement: str) -> Tuple[str, str]:
        sub_statement, operator = self.subequation_finder.get_subequation(statement)

        operator_index = sub_statement.index(operator.character)

        if operator.type == "unery":
            result = self.solve_unery_statement(operator_index, sub_statement, operator)
        else:
            result = self.solve_binary_statement(operator_index, sub_statement, operator)

        return sub_statement, result

    def solve_unery_statement(self, operator_index: int, sub_statement: str, operator: Operator) -> str:
        number = sub_statement[0:operator_index].replace("(", "")

        formatted_number = self.number_formatter.preprocess_number(number)
        result = operator.function(formatted_number)
        formatted_results = self.number_formatter.postprocess_number(result)

        return formatted_results

    def solve_binary_statement(self, operator_index: int, sub_statement: str, operator: Operator) -> str:
        first_number = sub_statement[0:operator_index].replace("(", "")
        second_number = sub_statement[operator_index + 1::].replace(")", "")

        formatted_first_number = self.number_formatter.preprocess_number(first_number)
        formatted_second_number = self.number_formatter.preprocess_number(second_number)

        result = operator.function(formatted_first_number, formatted_second_number)
        formatted_results = self.number_formatter.postprocess_number(result)

        return formatted_results

    def is_statement_solved(self, equation: str) -> bool:
        return self.subequation_finder.is_statement_solved(equation)
