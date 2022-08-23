from Parser import Parser

if __name__ == "__main__":
    import sys

    input_string = sys.argv[1]
    print(Parser.run(input_string))
