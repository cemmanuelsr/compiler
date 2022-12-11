import re


class PrePro:

    @staticmethod
    def _clean_comments(code: str):
        return re.sub(r"\s*%.*", "", code)

    @staticmethod
    def _replace_code_by_token(code: str):
        code = code.replace("\\times", "*")
        code = code.replace("\\gets", "<-")
        code = code.replace("\\sum", "Iterator")
        code = code.replace("\\eq", "=")
        code = code.replace("\\cup", ".")
        code = code.replace("\\lor", "|")
        code = code.replace("\\land", "&")
        code = code.replace("\\cdot", "*")
        code = code.replace("\\frac", "/")
        code = code.replace("\\neg", "!")
        code = code.replace("\\to", "->")
        return code

    @staticmethod
    def pre_process(code: str):
        code = PrePro._clean_comments(code)
        code = PrePro._replace_code_by_token(code)
        return code
