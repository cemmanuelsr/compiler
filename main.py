from parsers.Parser import Parser
from processes.PrePro import PrePro
from processes.Assembler import Assembler

if __name__ == "__main__":
    import sys
    from os import getenv

    environment = getenv('DEVELOPMENT', '0')

    file = sys.argv[1]
    filename = file.split('/')[-1].split('.')[:-1][0]
    if file.split('.')[-1] != 'carbon':
        raise Exception('You must pass a carbon file')

    with open(file, "r") as f:
        code = f.read()

    lines = code.split('\n')
    lines = [PrePro.pre_process(line).strip() for line in lines]
    code = '\n'.join(lines)

    root = Parser.run(code)
    Assembler.body = root.evaluate()
    Assembler.write(filename, path='assets/asm' if environment == '1' else '.')
