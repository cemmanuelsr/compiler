import unittest

from parsers.Parser import Parser


class TestParser(unittest.TestCase):

    def test_1(self):
        code = "   100   +  100  -100+  1"
        self.assertEqual(Parser.run(code).evaluate(), 101)

    def test_2(self):
        code = "1 1"
        self.assertRaises(Exception, Parser.run, code)

    def test_3(self):
        code = "(1+1)*3"
        self.assertEqual(Parser.run(code).evaluate(), 6)

    def test_4(self):
        code = "++--++2"
        self.assertEqual(Parser.run(code).evaluate(), 2)

    def test_5(self):
        code = "(1+1)*(2+2)"
        self.assertEqual(Parser.run(code).evaluate(), 8)

    def test_6(self):
        code = "(((1+1)))"
        self.assertEqual(Parser.run(code).evaluate(), 2)

    def test_7(self):
        code = "40--2"
        self.assertEqual(Parser.run(code).evaluate(), 42)

    def test_8(self):
        code = "40+-+-2"
        self.assertEqual(Parser.run(code).evaluate(), 42)


if __name__ == "__main__":
    unittest.main()
