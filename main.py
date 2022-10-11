from parsers.Parser import Parser
from processes.PrePro import PrePro

if __name__ == "__main__":
    import sys

    file = sys.argv[1]
    if file.split('.')[-1] != 'carbon':
        raise Exception('You must pass a carbon file')

    with open(file, "r") as f:
        code = f.read()

    Parser.run(code).evaluate()
