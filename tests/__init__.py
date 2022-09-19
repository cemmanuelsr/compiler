import unittest
from TestParser import TestParser
from TestTokenizer import TestTokenizer
from TestPrePro import TestPrePro
from parsers.Parser import Parser
from processes.PrePro import PrePro


class TestMain(unittest.TestCase):

    def test_1(self):
        file = "../assets/codes/test_1.carbon"
        with open(file, "r") as f:
            code = f.read()
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code).evaluate(), 101)

    def test_2(self):
        file = "../assets/codes/test_2.carbon"
        with open(file, "r") as f:
            code = f.read()
        code = PrePro.pre_process(code)
        self.assertRaises(Exception, Parser.run, code)

    def test_3(self):
        file = "../assets/codes/test_3.carbon"
        with open(file, "r") as f:
            code = f.read()
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code).evaluate(), 6)

    def test_4(self):
        file = "../assets/codes/test_4.carbon"
        with open(file, "r") as f:
            code = f.read()
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code).evaluate(), 2)

    def test_5(self):
        file = "../assets/codes/test_5.carbon"
        with open(file, "r") as f:
            code = f.read()
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code).evaluate(), 8)

    def test_6(self):
        file = "../assets/codes/test_6.carbon"
        with open(file, "r") as f:
            code = f.read()
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code).evaluate(), 2)

    def test_7(self):
        file = "../assets/codes/test_7.carbon"
        with open(file, "r") as f:
            code = f.read()
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code).evaluate(), 42)

    def test_8(self):
        file = "../assets/codes/test_8.carbon"
        with open(file, "r") as f:
            code = f.read()
        code = PrePro.pre_process(code)
        self.assertEqual(Parser.run(code).evaluate(), 42)


if __name__ == "__main__":
    unittest.main()
