"""
Name: base_number_formatter.py
Author: Almog Maimon
Purpose:
Date: 02/10/2022
"""


class BaseNumberFormatter:
    def preprocess_number(self, number: str) -> int:
        pass

    def postprocess_number(self, number: int) -> str:
        pass
