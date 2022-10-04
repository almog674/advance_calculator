"""
Name: test_parenthesis_hadle.py
Author: Almog Maimon
Purpose:
Date: 04/10/2022
"""

import pytest

from parenthesis_handler.parenthesis_validator import ParenthesisValidator


@pytest.mark.parametrize("parenthesis", ["()", "()()", "(()(())())", ""])
def test_parenthesis_validation_valid(parenthesis):
    parenthesis_validator = ParenthesisValidator()

    assert parenthesis_validator.is_parenthesis_valid(parenthesis)


@pytest.mark.parametrize("parenthesis", ["(", "(()", "(()(()", ")(", "())()("])
def test_parenthesis_validation_invalid(parenthesis):
    parenthesis_validator = ParenthesisValidator()

    assert not parenthesis_validator.is_parenthesis_valid(parenthesis)
