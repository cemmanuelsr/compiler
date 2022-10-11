import unittest

from parsers.Parser import Parser


class TestParser(unittest.TestCase):

    def test_1(self):
        file = "assets/codes/test_1.carbon"
        with open(file, "r") as f:
            code = f.read()
        self.assertEqual(Parser.run(code).evaluate(), 101)

    def test_2(self):
        file = "assets/codes/test_2.carbon"
        with open(file, "r") as f:
            code = f.read()
        self.assertEqual(Parser.run(code).evaluate(), 101)


if __name__ == "__main__":
    unittest.main()
