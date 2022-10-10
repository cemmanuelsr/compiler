import re


class PrePro:

    @staticmethod
    def _clean_comments(code: str):
        return re.sub(r"\s*//.*", "", code)

    @staticmethod
    def pre_process(code: str):
        code = PrePro._clean_comments(code)
        return code
