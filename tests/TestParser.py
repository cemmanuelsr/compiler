import unittest
from unittest import mock
from io import StringIO
import sys

from processes.PrePro import PrePro
from processes.WriteDotFile import Writer
from parsers.Parser import Parser
from tables import symbol_table


class CapturingStdOut(list):
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
        Writer.write('test_1', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['101'])
        symbol_table.table = {}

    def test_2(self):
        file = "../assets/codes/test_2.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_2', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['5', '4', '5', '6'])
        symbol_table.table = {}

    def test_3(self):
        file = "../assets/codes/test_3.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_3', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, [])
        symbol_table.table = {}

    def test_4(self):
        file = "../assets/codes/test_4.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        with self.assertRaises(Exception) as output:
            Parser.run(code)
        Writer.write_exception(str(output.exception), Parser.last_node)
        Writer.write('test_4', path='../graphs/dot')
        symbol_table.table = {}

    def test_5(self):
        file = "../assets/codes/test_5.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_5', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1'])
        symbol_table.table = {}

    def test_6(self):
        file = "../assets/codes/test_6.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_5', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['3'])
        symbol_table.table = {}

    def test_7(self):
        file = "../assets/codes/test_7.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_7', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['2'])
        symbol_table.table = {}

    @mock.patch('builtins.input', side_effect=['7'])
    def test_8(self, mock_input):
        file = "../assets/codes/test_8.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_8', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['7'])
        symbol_table.table = {}

    @mock.patch('builtins.input', side_effect=['2', '8'])
    def test_9(self, mock_input):
        file = "../assets/codes/test_9.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_9', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['10'])
        symbol_table.table = {}

    @mock.patch('builtins.input', side_effect=['19'])
    def test_10(self, mock_input):
        file = "../assets/codes/test_10.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_10', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['19'])
        symbol_table.table = {}

    def test_11(self):
        file = "../assets/codes/test_11.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        with self.assertRaises(Exception) as output:
            Parser.run(code)
        Writer.write_exception(str(output.exception), Parser.last_node)
        Writer.write('test_11', path='../graphs/dot')
        symbol_table.table = {}

    def test_12(self):
        file = "../assets/codes/test_12.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        with self.assertRaises(Exception) as output:
            Parser.run(code)
        Writer.write_exception(str(output.exception), Parser.last_node)
        Writer.write('test_12', path='../graphs/dot')
        symbol_table.table = {}

    def test_13(self):
        file = "../assets/codes/test_13.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        with self.assertRaises(Exception) as output:
            Parser.run(code)
        Writer.write_exception(str(output.exception), Parser.last_node)
        Writer.write('test_13', path='../graphs/dot')
        symbol_table.table = {}

    def test_14(self):
        file = "../assets/codes/test_14.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_14', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['4'])
        symbol_table.table = {}

    def test_15(self):
        file = "../assets/codes/test_15.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_15', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1'])
        symbol_table.table = {}

    def test_16(self):
        file = "../assets/codes/test_16.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_16', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1', '2'])
        symbol_table.table = {}

    def test_17(self):
        file = "../assets/codes/test_17.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_17', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['2'])
        symbol_table.table = {}

    def test_18(self):
        file = "../assets/codes/test_18.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_18', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1'])
        symbol_table.table = {}

    def test_19(self):
        file = "../assets/codes/test_19.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_19', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1'])
        symbol_table.table = {}

    def test_20(self):
        file = "../assets/codes/test_20.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_20', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1'])
        symbol_table.table = {}

    def test_21(self):
        file = "../assets/codes/test_21.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_21', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1'])
        symbol_table.table = {}

    def test_22(self):
        file = "../assets/codes/test_22.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_22', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['2'])
        symbol_table.table = {}

    def test_23(self):
        file = "../assets/codes/test_23.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_23', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1', '2', '3'])
        symbol_table.table = {}

    def test_24(self):
        file = "../assets/codes/test_24.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_24', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1', '2', '3'])
        symbol_table.table = {}

    def test_25(self):
        file = "../assets/codes/test_25.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_25', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1', '2', '3', '4', '5', '5'])
        symbol_table.table = {}

    def test_26(self):
        file = "../assets/codes/test_26.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        with self.assertRaises(Exception) as output:
            Parser.run(code)
        Writer.write_exception(str(output.exception), Parser.last_node)
        Writer.write('test_26', path='../graphs/dot')
        symbol_table.table = {}

    @mock.patch('builtins.input', side_effect=['3', '0'])
    def test_27(self, mock_input):
        file = "../assets/codes/test_27.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_27', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['3', '3', '2', '1', '0'])
        symbol_table.table = {}

    def test_28(self):
        file = "../assets/codes/test_28.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_28', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1'])
        symbol_table.table = {}

    def test_29(self):
        file = "../assets/codes/test_29.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_29', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['3', '1', '2', '2', '0', '0', '1'])
        symbol_table.table = {}

    def test_30(self):
        file = "../assets/codes/test_30.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_30', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['abcdef', 'abc1', '1abc', '12', 'abc1', '1', '1', '0'])
        symbol_table.table = {}

    def test_31(self):
        file = "../assets/codes/test_31.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_31', path='../graphs/dot')
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['0'])
        symbol_table.table = {}

    def test_32(self):
        file = "../assets/codes/test_32.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        with self.assertRaises(Exception) as output:
            root.evaluate(symbol_table)
        Writer.write_exception(str(output.exception), Parser.last_node)
        Writer.write('test_32', path='../graphs/dot')
        symbol_table.table = {}


if __name__ == "__main__":
    unittest.main()
