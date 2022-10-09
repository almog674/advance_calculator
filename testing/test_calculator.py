import pytest

from calculator import Calculator
from calculator_builder.calculator_builder import CalculatorBuilder


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
