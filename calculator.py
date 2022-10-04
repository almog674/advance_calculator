"""
Things that must change:
    1. The operators in the initialization must be injected to the class
    2. The format of the operators rather be a dataclass.
    3. Create UI class for input/output.
    4. Create a better module to deal with parenthesis.
    5. Refactor "get_statement_index".
    6. Give better naming for basically everything.

"""
from operators_manager.base_operators_manager import BaseOperatorsManager
from statements_solver import StatementsSolver
from sunequation_finder import SubequationFinder


class Calculator:
    def __init__(self, statements_solver: StatementsSolver):
        self.statements_solver = statements_solver

        # self.run()

    def run(self):
        while True:
            equation = input("Write a statement: ")
            equation = equation.replace(" ", '')
            result = self.calc(equation)
            print(f"The final results: {result}")

    def calculate(self, equation: str) -> str:
        # Check if the equation is valid

        if self.statements_solver.is_statement_solved(equation):
            return equation

        print(equation, " can be solved")

        subequation, result = self.statements_solver.solve_statement(equation)

        new_equation = equation.replace(subequation, result)
        return self.calculate(new_equation)

    # def calc(self, equation):
    #     there_is_parentesis, parentesis_equation, sub_statement = self.handle_parentesis(
    #         equation)
    #
    #     while there_is_parentesis:
    #         result = self.calc(parentesis_equation)
    #         equation = equation.replace(sub_statement, result)
    #         there_is_parentesis, parentesis_equation, sub_statement = self.handle_parentesis(
    #             equation)
    #
    #     new_equation = self.get_strongerst_action(equation)
    #
    #     if equation == new_equation:
    #         return equation
    #     else:
    #         return self.calc(new_equation)

    # def handle_parentesis(self, equation):
    #     # There is an error, no checking if the parenthesis is even valid.
    #
    #     # Better naming!
    #     if '(' in equation:
    #         first_index = equation.rfind('(')
    #         new_eq = equation[first_index::]
    #         second_index = first_index + new_eq.index(')')
    #         parentesis_equation = equation[first_index +
    #                                        1:second_index]
    #         sub_statement = equation[first_index:second_index + 1]
    #         return True, parentesis_equation, sub_statement
    #     else:
    #         return False, None, None
    #
    # def get_statement_index(self, equation, operator_index):
    #     start_index = operator_index - 1
    #     end_index = operator_index + 1
    #
    #     char = equation[start_index]
    #
    #     while True:
    #         if not (char.isnumeric() or char == '.' or char == '~'):
    #             start_index += 2
    #             break
    #
    #         elif (start_index == 0):
    #             break
    #
    #         else:
    #             char = equation[start_index]
    #         start_index -= 1
    #
    #     char = equation[end_index]
    #     while True:
    #         if not (char.isnumeric() or char == '.' or char == '~'):
    #             end_index -= 1
    #             print("break")
    #             break
    #         elif end_index > len(equation) - 1:
    #             end_index += 1
    #             break
    #         else:
    #             char = equation[end_index]
    #         end_index += 1
    #
    #     sub_statement = equation[start_index:end_index]
    #     first_num = equation[start_index:operator_index]
    #     second_num = equation[operator_index + 1: end_index]
    #
    #     return sub_statement, first_num, second_num
    #
    # def get_unery_statement_index(self, equation, operator_index):
    #     end_index = operator_index + 1
    #     char = equation[end_index]
    #
    #     while True:
    #         if not (char.isnumeric() or char == '.' or char == '~'):
    #             end_index -= 1
    #             print("break")
    #             break
    #         elif (end_index > len(equation) - 1):
    #             end_index += 1
    #             break
    #         else:
    #             char = equation[end_index]
    #         end_index += 1
    #
    #     sub_statement = equation[operator_index:end_index]
    #     first_num = equation[operator_index + 1:end_index]
    #     return sub_statement, first_num
    #
    # def binary_operator(self, equation, index, letter):
    #     sub_statement, first_number, second_number = self.get_statement_index(
    #         equation, operator_index=index)
    #
    #     first_number = self.preprocess_number(first_number)
    #     second_number = self.preprocess_number(second_number)
    #
    #     func = self.operators[letter][0]
    #
    #     print(
    #         f"Subequation: {first_number} {equation[index]} {second_number} --- {sub_statement}")
    #
    #     result = func(first_number, second_number)
    #     result = self.postprocess_result(result)
    #
    #     equation = equation.replace(sub_statement, result)
    #
    #     return equation
    #
    # def unery_operator(self, equation, index, letter):
    #     sub_statement, first_number = self.get_unery_statement_index(
    #         equation, index)
    #     first_number = self.preprocess_number(first_number)
    #     func = self.operators[letter][0]
    #     print(
    #         f"Subequation: {equation[index]} {first_number} --- {sub_statement}")
    #     result = func(first_number)
    #     result = self.postprocess_result(result)
    #     equation = equation.replace(sub_statement, result)
    #     return equation
    #
    # def get_strongerst_action(self, equation):
    #     number = 6
    #     while number > 0:
    #         actions = [k for (k, v) in self.operators.items()
    #                    if v[1] == number]
    #
    #         for i, letter in enumerate(equation):
    #             if letter in actions:
    #                 if self.operators[letter][2] == 'binary':
    #                     equation = self.binary_operator(equation, i, letter)
    #                 else:
    #                     equation = self.unery_operator(equation, i, letter)
    #                 return equation
    #         number -= 1
    #     return equation

    def preprocess_number(self, number):
        if number[0] == '~':
            number = -round(float(number[1::]), 2)
        else:
            number = round(float(number), 2)
        return number

    def postprocess_result(self, result):
        result = str(result)

        # Handle scientific notation
        if 'e' in result:
            result = float(result)
            result = "{:.1f}".format(result)

        result = str(result)
        result = result.replace('-', '~')
        return result
