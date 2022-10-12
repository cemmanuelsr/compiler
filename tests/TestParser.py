import unittest
from io import StringIO
import sys

from processes.PrePro import PrePro
from processes.WriteDotFile import Writer
from parsers.Parser import Parser


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class TestParser(unittest.TestCase):

    def test_1(self):
        file = "../assets/codes/test_1.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write(root, 'test_1', path='../graphs/dot')
        with Capturing() as output:
            root.evaluate()
        self.assertEqual(output, ['101'])

    def test_2(self):
        file = "../assets/codes/test_2.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write(root, 'test_2', path='../graphs/dot')
        with Capturing() as output:
            root.evaluate()
        self.assertEqual(output, ['5','4','5','6'])

    def test_3(self):
        file = "../assets/codes/test_3.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write(root, 'test_3', path='../graphs/dot')
        with Capturing() as output:
            root.evaluate()
        self.assertEqual(output, [])

    def test_4(self):
        file = "../assets/codes/test_4.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        self.assertRaises(Exception, Parser.run, code)

    def test_5(self):
        file = "../assets/codes/test_5.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write(root, 'test_5', path='../graphs/dot')
        with Capturing() as output:
            root.evaluate()
        self.assertEqual(output, ['1'])

    def test_6(self):
        file = "../assets/codes/test_6.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        self.assertRaises(Exception, Parser.run, code)

    def test_7(self):
        file = "../assets/codes/test_7.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write(root, 'test_7', path='../graphs/dot')
        with Capturing() as output:
            root.evaluate()
        self.assertEqual(output, ['2'])

    # def test_8(self):
    #     file = "../assets/codes/test_8.carbon"
    #     with open(file, "r") as f:
    #         code = f.read()
    #     lines = code.split('\n')
    #     lines = [PrePro.pre_process(line).strip() for line in lines]
    #     code = '\n'.join(lines)
    #     root = Parser.run(code)
    #     Writer.write(root, 'test_8', path='../graphs/dot')
    #     with Capturing() as output:
    #         root.evaluate()
    #     self.assertEqual(output, ['7'])
    #
    # def test_9(self):
    #     file = "../assets/codes/test_9.carbon"
    #     with open(file, "r") as f:
    #         code = f.read()
    #     lines = code.split('\n')
    #     lines = [PrePro.pre_process(line).strip() for line in lines]
    #     code = '\n'.join(lines)
    #     root = Parser.run(code)
    #     Writer.write(root, 'test_9', path='../graphs/dot')
    #     with Capturing() as output:
    #         root.evaluate()
    #     self.assertEqual(output, ['10'])
    #
    # def test_10(self):
    #     file = "../assets/codes/test_10.carbon"
    #     with open(file, "r") as f:
    #         code = f.read()
    #     lines = code.split('\n')
    #     lines = [PrePro.pre_process(line).strip() for line in lines]
    #     code = '\n'.join(lines)
    #     root = Parser.run(code)
    #     Writer.write(root, 'test_10', path='../graphs/dot')
    #     with Capturing() as output:
    #         root.evaluate()
    #     self.assertEqual(output, ['19'])

    def test_11(self):
        file = "../assets/codes/test_11.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        self.assertRaises(Exception, Parser.run, code)

    def test_12(self):
        file = "../assets/codes/test_12.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        self.assertRaises(Exception, Parser.run, code)

    def test_13(self):
        file = "../assets/codes/test_12.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        self.assertRaises(Exception, Parser.run, code)


if __name__ == "__main__":
    unittest.main()