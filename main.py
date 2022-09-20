from parsers.Parser import Parser
from processes.PrePro import PrePro

if __name__ == "__main__":
    import sys

    file = sys.argv[1]
    if file.split('.')[-1] != 'carbon':
        raise Exception('You must pass a carbon file')

    with open(file, "r") as f:
        code = f.read()

    lines = code.split('\n')
    code = ""
    for line in lines:
        code += PrePro.pre_process(line).strip()

    Parser.run(code).evaluate()
