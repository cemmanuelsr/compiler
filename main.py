from processes.PrePro import PrePro
from parsers.Parser import Parser

if __name__ == "__main__":
    import sys

    codes = sys.argv[1:]
    for code in codes:
        code = PrePro.pre_process(code)
        print(Parser.run(code).evaluate())
