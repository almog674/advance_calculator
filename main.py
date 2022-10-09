"""
Name: main.py
Author: Almog Maimon
Purpose:
Date: 01/10/2022
"""
from calculator import Calculator
from utils.constants import SPECIAL_OPERATORS
from operators_manager.custom_operator import Operator
from utils.math_operations import get_min, get_mean, get_max, modulu, factorial, power, multiply, divide, addition, \
    subtraction
from number_formatter.build_pipline_formatter import BuildPiplineFormatter
from operators_manager.operators_manager import DictOperationsManager
from parenthesis_handler.parenthesis_handler import ParenthesisHandler
from parenthesis_handler.parenthesis_validator import ParenthesisValidator
from statements_solver import StatementsSolver
from sunequation_finder import SubequationFinder


def main():
    operators = {'&': Operator("min", get_min, 5, "binary"), '$': Operator("$", get_max, 5, "binary"),
                 '@': Operator("@", get_mean, 5, "binary"), '%': Operator("%", modulu, 4, "binary"),
                 '!': Operator("!", factorial, 4, "unery"), '^': Operator("^", power, 3, "binary"),
                 '*': Operator("*", multiply, 2, "binary"), '/': Operator("/", divide, 2, "binary"),
                 '+': Operator("+", addition, 1, "binary"), '-': Operator("-", subtraction, 1, "binary")}

    operations_manager = DictOperationsManager(operators)
    numbers_formatter_builder = BuildPiplineFormatter()
    numbers_formatter = numbers_formatter_builder.build_pipline_formatter()

    parenthesis_handler = ParenthesisHandler(ParenthesisValidator())
    subequation_finder = SubequationFinder(operations_manager, parenthesis_handler, SPECIAL_OPERATORS)
    statements_solver = StatementsSolver(subequation_finder, numbers_formatter)
    calculator = Calculator(statements_solver)

    print(calculator.calculate("5/(4-(3+2))*2"))


if __name__ == '__main__':
    main()
