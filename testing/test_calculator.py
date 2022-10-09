import pytest
import change_path_for_testing
from calculator_builder.calculator_builder import CalculatorBuilder

from parenthesis_handler.parenthesis_handler import ParenthesisHandler
from parenthesis_handler.parenthesis_validator import ParenthesisValidator

from calculator import Calculator
from utils.constants import SPECIAL_OPERATORS
from operators_manager.custom_operator import Operator
from utils.math_operations import get_min, get_mean, get_max, modulu, factorial, power, multiply, divide, addition, \
    subtraction
from number_formatter.build_pipline_formatter import BuildPiplineFormatter
from operators_manager.operators_manager import DictOperationsManager
from statements_solver import StatementsSolver
from sunequation_finder import SubequationFinder


@pytest.fixture(scope="module")
def calculator():
    """Creates a basic calculator for the test."""
    calculator_builder = CalculatorBuilder()
    calculator = calculator_builder.build_calculator()

    return calculator


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


def test_calculation_with_floats(calculator: Calculator):
    assert calculator.calculate("1.342*5.32-(23.1/42.12)") == "6.58"
