"""
Name: operators_manager.py
Author: Almog Maimon
Purpose: Manage the operators of a certain calculator.
Date: 01/10/2022
"""
from typing import Tuple, Dict

from custom_operator import Operator
from operators_manager.base_operators_manager import BaseOperatorsManager


class DictOperationsManager(BaseOperatorsManager):
    def __init__(self, operations: Dict):
        self.operations = operations

    def add_operator(self, operator_information: Operator) -> None:
        self.operations[operator_information.character] = operator_information

    def delete_operator(self, operator_character: str) -> None:
        if self.operations.get(operator_character):
            self.operations.pop(operator_character)

    def get_equation_strongest_operator(self, equation: str) -> Tuple[int, Operator]:
        """
        Returns the index & Operator object of the strongest operator in
        the equation, for example in 3+4*12, "*" is the strongest operator.
        """
        operation, operation_index, operation_priority = None, None, 0

        for i, character in enumerate(equation):
            if character in list(self.operations.keys()):
                current_operation_priority = self.operations.get(character).priority

                if current_operation_priority > operation_priority:
                    operation_index = i
                    operation_priority = current_operation_priority
                    operation = self.operations.get(character)

        return operation_index, operation
