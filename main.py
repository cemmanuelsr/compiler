from parsers.Parser import Parser

if __name__ == "__main__":
    import sys

    file = sys.argv[1]
    with open(file, "r") as f:
        code = f.read()
    print(Parser.run(code).evaluate())
