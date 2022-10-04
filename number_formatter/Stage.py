"""
Name: Stage.py
Author: Almog Maimon
Purpose:
Date: 03/10/2022
"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Stage:
    name: str
    function: Callable
    description: str = "There is no description for this."

    def __repr__(self):
        return f"{self.name} -> {self.description}"
