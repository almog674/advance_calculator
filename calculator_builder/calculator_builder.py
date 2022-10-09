from calculator import Calculator
from number_formatter.build_pipline_formatter import BuildPiplineFormatter
from operators_manager.custom_operator import Operator
from operators_manager.operators_manager import DictOperationsManager
from parenthesis_handler.parenthesis_handler import ParenthesisHandler
from parenthesis_handler.parenthesis_validator import ParenthesisValidator
from statements_solver import StatementsSolver
from sunequation_finder import SubequationFinder
from utils.constants import SPECIAL_OPERATORS
from utils.math_operations import get_min, get_mean, factorial, multiply, addition, subtraction, divide, power, modulu, \
    get_max


class CalculatorBuilder:
    def __init__(self):
        pass

    def build_calculator(self) -> Calculator:
        # Stages

        # 1. Build the operators
        operators = {'&': Operator("&", get_min, 5, "binary"), '$': Operator("$", get_max, 5, "binary"),
                     '@': Operator("@", get_mean, 5, "binary"), '%': Operator("%", modulu, 4, "binary"),
                     '!': Operator("!", factorial, 4, "unery"), '^': Operator("^", power, 3, "binary"),
                     '*': Operator("*", multiply, 2, "binary"), '/': Operator("/", divide, 2, "binary"),
                     '+': Operator("+", addition, 1, "binary"), '-': Operator("-", subtraction, 1, "binary")}

        # 1.1 Create the operators manager
        operations_manager = DictOperationsManager(operators)

        # 2 Build the numbers formatter
        numbers_formatter_builder = BuildPiplineFormatter()
        numbers_formatter = numbers_formatter_builder.build_pipline_formatter()

        # 3. Build the parenthesis handler
        parenthesis_handler = ParenthesisHandler(ParenthesisValidator())
        subequation_finder = SubequationFinder(operations_manager, parenthesis_handler, SPECIAL_OPERATORS)

        # 4. Build the statements_solver
        statements_solver = StatementsSolver(subequation_finder, numbers_formatter)

        return Calculator(statements_solver)
