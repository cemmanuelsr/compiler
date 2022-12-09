import unittest
from unittest import mock
from io import StringIO
import sys

from processes.PrePro import PrePro
from processes.WriteDotFile import Writer
from parsers.Parser import Parser
from tables.SymbolTable import SymbolTable


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

    def basic_test(self):
        file = "../assets/codes/basic_test.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('basic_test', path='../graphs/dot')
        symbol_table = SymbolTable()
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['1'])

    @mock.patch('builtins.input', side_effect=['3', '0'])
    def test_function_call(self, mock_input):
        file = "../assets/codes/test_function_call.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_function_call', path='../graphs/dot')
        symbol_table = SymbolTable()
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['3', '3', '2', '1', '0'])

    def test_int_operations(self):
        file = "../assets/codes/test_int_operations.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_int_operations', path='../graphs/dot')
        symbol_table = SymbolTable()
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['3', '1', '2', '2', '0', '0', '1'])

    def test_str_operations(self):
        file = "../assets/codes/test_str_operations.carbon"
        with open(file, "r") as f:
            code = f.read()
        lines = code.split('\n')
        lines = [PrePro.pre_process(line).strip() for line in lines]
        code = '\n'.join(lines)
        root = Parser.run(code)
        Writer.write('test_str_operations', path='../graphs/dot')
        symbol_table = SymbolTable()
        with CapturingStdOut() as output:
            root.evaluate(symbol_table)
        self.assertEqual(output, ['abcdef', 'abc1', '1abc', '12', 'abc1', '1', '1', '0'])


if __name__ == "__main__":
    unittest.main()
