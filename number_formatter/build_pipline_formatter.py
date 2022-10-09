"""
Name: build_pipline_formatter.py
Author: Almog Maimon
Purpose: Helps you build to pipline formatter with ease.
Date: 04/10/2022
"""
from utils.constants import Pipelines
from number_formatter.base_build_pipline_formatter import BaseBuildPiplineFormatter
from number_formatter.format_functions import format_negative_number, round_number, handle_scientific_notation, \
    replace_special_minus_notation
from number_formatter.pipline_number_formatter import PiplineNumberFormatter


class BuildPiplineFormatter(BaseBuildPiplineFormatter):
    def build_pipline_formatter(self) -> PiplineNumberFormatter:
        pipline_formatter = PiplineNumberFormatter()
        self._build_pre_pipline(pipline_formatter)
        self._build_post_pipline(pipline_formatter)

        return pipline_formatter

    @staticmethod
    def _build_pre_pipline(pipline_formatter: PiplineNumberFormatter):
        pipline_formatter.add_function_to_pipline(format_negative_number, Pipelines.PREPROCESS)
        pipline_formatter.add_function_to_pipline(round_number, Pipelines.PREPROCESS)

    @staticmethod
    def _build_post_pipline(pipline_formatter: PiplineNumberFormatter):
        pipline_formatter.add_function_to_pipline(handle_scientific_notation, Pipelines.POSTPROCESS)
        pipline_formatter.add_function_to_pipline(replace_special_minus_notation, Pipelines.POSTPROCESS)
