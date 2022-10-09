"""
Name: abstract_parenthesis_handler.py
Author: Almog Maimon
Purpose: An interface for handling parenthesis in an equation
Date: 01/10/2022
"""
from abc import ABC, abstractmethod
from typing import Tuple

from parenthesis_handler.parenthesis_validator import ParenthesisValidator


class InvalidParenthesis(Exception):
    """
    Description: The equation have an unmatched parenthesis.
    Example: ([){).
    """

    def __init__(self, message: str):
        self.message = message


class AbstractParenthesisHandler(ABC):
    """
    Handles the parenthesis in an equation.
    """

    def __init__(self, parenthesis_validator: ParenthesisValidator):
        self.parenthesis_validator = parenthesis_validator

    @staticmethod
    def _get_equation_inside_parenthesis(equation: str) -> Tuple[str, str]:
        raise NotImplementedError()

    @staticmethod
    def handle_parenthesis(equation: str) -> Tuple[bool, str, str]:
        raise NotImplementedError()
