from typing import Callable

from constants import Pipelines
from number_formatter.Stage import Stage
from number_formatter.base_number_formatter import BaseNumberFormatter


class PiplineNumberFormatter(BaseNumberFormatter):
    def __init__(self):
        self.preprocess_pipline = []
        self.postprocess_pipline = []

        self.piplines = {Pipelines.PREPROCESS: self.preprocess_pipline, Pipelines.POSTPROCESS: self.postprocess_pipline}

    def preprocess_number(self, number: str) -> float:
        for stage in self.preprocess_pipline:
            number = stage.function(number)

        return float(number)

    def postprocess_number(self, number: int) -> str:
        number = str(number)

        for stage in self.postprocess_pipline:
            number = stage.function(number)

        return number

    def add_stage_to_pipline(self, stage: Stage, pipline_name: str):
        self._validate_pipline(pipline_name)
        pipline = self.piplines.get(pipline_name)

        pipline.append(stage)

    def add_function_to_pipline(self, function: Callable, pipline_name: str):
        stage = Stage(function.__name__, function, function.__doc__)

        self.add_stage_to_pipline(stage, pipline_name)

    def remove_stage_from_pipline(self, pipline_name: str, index: int):
        self._validate_pipline(pipline_name)
        pipline = self.piplines.get(pipline_name)
        self._validate_index_accessing_to_pipline(pipline, index)

        pipline.pop(index)

    def show_pipline(self, pipline_name: str):
        self._validate_pipline(pipline_name)
        pipline = self.piplines.get(pipline_name)

        print(f"Stages of {pipline_name}")
        for index, stage in enumerate(pipline):
            print(f"id {index}: {stage}")

    def _validate_pipline(self, pipline_name: str):
        if not isinstance(self.piplines.get(pipline_name), list):
            raise ValueError(
                f"Pipline {pipline_name} does not exists, please choose {Pipelines.PREPROCESS} or {Pipelines.POSTPROCESS}")

    @staticmethod
    def _validate_index_accessing_to_pipline(pipline: list, index: int):
        if len(pipline) < index:
            raise IndexError(
                f"Trying to access stage index {index + 1} but the length of the pipline is {len(pipline)}.")
