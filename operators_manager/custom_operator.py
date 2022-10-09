"""
Name: custom_operator.py
Author: Almog Maimon
Purpose: Represent a mathematic operator.
Date: 01/10/2022
"""
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Operator:
    character: str
    function: Callable
    priority: int
    type: str
