import unittest

from processes.PrePro import PrePro
from parsers.Parser import Parser


class TestTokenizer(unittest.TestCase):

    def test_1(self):
        code = "   100   +  100  -100+  1"
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code), 101)

    def test_2(self):
        code = "1 1"
        code = PrePro.pre_process(code)
        self.assertRaises(Exception, Parser.run, code)

    def test_3(self):
        code = "(1+1)*3"
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code), 6)

    def test_4(self):
        code = "++--++2"
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code), 2)

    def test_5(self):
        code = "(1+1)*(2+2)"
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code), 8)

    def test_6(self):
        code = "(((1+1)))"
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code), 2)

    def test_7(self):
        code = "40--2"
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code), 42)

    def test_8(self):
        code = "40+-+-2"
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code), 42)

if __name__ == "__main__":
    unittest.main()
