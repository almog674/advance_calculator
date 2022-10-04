"""
Name: test_handle_parenthesis.py
Author: Almog Maimon
Purpose:
Date: 04/10/2022
"""
import pytest

from parenthesis_handler.abstract_parenthesis_handler import InvalidParenthesis
from parenthesis_handler.parenthesis_handler import ParenthesisHandler
from parenthesis_handler.parenthesis_validator import ParenthesisValidator


@pytest.fixture(scope="module")
def parenthesis_handler():
    return ParenthesisHandler(ParenthesisValidator())


def test_handle_parenthesis_invalid(parenthesis_handler: ParenthesisHandler):
    """
    Checks the parenthesis_handle with invalid parenthesis.
    Asserting that an "InvalidParenthesis" will be raised.
    """
    with pytest.raises(InvalidParenthesis) as error_message:
        parenthesis_handler.handle_parenthesis("()(")


def test_handle_parenthesis_valid(parenthesis_handler: ParenthesisHandler):
    """Checks the parenthesis_handle with a valid equation."""
    assert parenthesis_handler.handle_parenthesis("(2+4)") == (True, "(2+4)", "2+4")


def test_handle_parenthesis_nested(parenthesis_handler: ParenthesisHandler):
    """Checks the parenthesis_handle with nested parenthesis."""
    assert parenthesis_handler.handle_parenthesis("(2+(4-3))") == (True, "(4-3)", "4-3")


def test_handle_parenthesis_no_parenthesis(parenthesis_handler: ParenthesisHandler):
    """Checks the parenthesis_handle with an equation without parenthesis."""
    assert parenthesis_handler.handle_parenthesis("4-3") == (False, "", "")
