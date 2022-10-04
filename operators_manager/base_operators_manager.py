"""
Name: base_operators_manager.py
Author: Almog Maimon
Purpose: An interface for controlling the operators of a calculator.
Date: 01/10/2022
"""
from typing import Tuple

from custom_operator import Operator


class BaseOperatorsManager:
    def add_operator(self, operator_information: Operator):
        raise NotImplementedError()

    def delete_operator(self, operator_character: str):
        raise NotImplementedError()

    def get_equation_strongest_operator(self, equation: str) -> Tuple[int, Operator]:
        raise NotImplementedError()
