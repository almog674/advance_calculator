"""
Name: constants.py
Author: Almog Maimon
Purpose: Hold the constants for the calculator.
Date: 01/10/2022
"""


class Operators:
    NEGATIVE_NUMBER = "~"
    ADDITION = "+"
    SUBTRATION = "-"

class Notations:
    SCIENTIFIC = "e"
    POINT = "."


SPECIAL_OPERATORS = [Operators.NEGATIVE_NUMBER, Notations.POINT]
ROUND_DIGITS = 2


class Pipelines:
    PREPROCESS = "pre"
    POSTPROCESS = "post"