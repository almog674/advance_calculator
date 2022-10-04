import pytest
import change_path_for_testing

from parenthesis_handler.parenthesis_handler import ParenthesisHandler
from parenthesis_handler.parenthesis_validator import ParenthesisValidator

from calculator import Calculator
from constants import SPECIAL_OPERATORS
from custom_operator import Operator
from math_operations import get_min, get_mean, get_max, modulu, factorial, power, multiply, divide, addition, \
    subtraction
from number_formatter.build_pipline_formatter import BuildPiplineFormatter
from operators_manager.operators_manager import DictOperationsManager
from statements_solver import StatementsSolver
from sunequation_finder import SubequationFinder


@pytest.fixture(scope="module")
def calculator():
    """Creates a basic calculator for the test."""
    operators = {'&': Operator("&", get_min, 5, "binary"), '$': Operator("$", get_max, 5, "binary"),
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
    return Calculator(statements_solver)


def test_basic_calculation(calculator: Calculator):
    assert calculator.calculate("4+3") == "7.0"


def test_calculation_two_steps(calculator: Calculator):
    assert calculator.calculate("4-3*2") == "~2.0"


def test_calculation_parenthesis(calculator: Calculator):
    assert calculator.calculate("5/(4-3)*2") == "10.0"


def test_calculation_double_parenthesis(calculator: Calculator):
    assert calculator.calculate("5/(4-(3+2))*2") == "~10.0"

def test_calculation_parenthesis_complex(calculator: Calculator):
    assert calculator.calculate("5/(4-(3+2))*(2-3)/(2^3)") == "0.625"
