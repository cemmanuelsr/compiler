import re


class PrePro:

    @staticmethod
    def _clean_comments(code: str):
        return re.sub(r"\s*//.*", "", code)

    @staticmethod
    def _clean_spaces(code: str):
        op_space_num = re.search(r"[+|\-|*|\\/]\s+\d", code)
        while op_space_num:
            code = code[:op_space_num.start() + 1] + code[op_space_num.end() - 1:]
            op_space_num = re.search(r"[+|\-|*|\\/]\s+\d", code)

        num_space_op = re.search(r"\d\s+[+|\-|*|\\/]", code)
        while num_space_op:
            code = code[:num_space_op.start() + 1] + code[num_space_op.end() - 1:]
            num_space_op = re.search(r"\d\s+[+|\-|*|\\/]", code)

        return code

    @staticmethod
    def pre_process(code: str):
        code = PrePro._clean_comments(code)
        code = PrePro._clean_spaces(code)
        return code
