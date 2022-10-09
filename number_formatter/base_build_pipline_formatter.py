from number_formatter.pipline_number_formatter import PiplineNumberFormatter


class BaseBuildPiplineFormatter:
    def build_pipline_formatter(self) -> PiplineNumberFormatter:
        raise NotImplementedError()

    @staticmethod
    def _build_pre_pipline(pipline_formatter: PiplineNumberFormatter):
        raise NotImplementedError()

    @staticmethod
    def _build_post_pipline(pipline_formatter: PiplineNumberFormatter):
        raise NotImplementedError
