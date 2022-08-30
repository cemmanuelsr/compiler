import unittest

from processes.PrePro import PrePro
from processes.Tokenizer import Tokenizer
from tokens.NumericToken import NumericToken
from tokens.OperatorToken import PlusToken, MultToken
from tokens.EOFToken import EOFToken


class TestTokenizer(unittest.TestCase):

    def test_invalid_token(self):
        code = "42 ,"
        tokenizer = Tokenizer(code + '\0')

        tokenizer.select_next()

        self.assertRaises(Exception, tokenizer.select_next)

    def test_tokenizer(self):
        code = "1    + 20  *3//some comment here"
        code = PrePro.pre_process(code)

        tokenizer = Tokenizer(code + '\0')
        tokenizer.select_next() # tokenizer.next = 1

        self.assertIsInstance(tokenizer.next, NumericToken)
        self.assertEqual(tokenizer.next.value, 1)

        tokenizer.select_next() # tokenizer.next = +

        self.assertIsInstance(tokenizer.next, PlusToken)

        tokenizer.select_next() # tokenizer.next = 20

        self.assertIsInstance(tokenizer.next, NumericToken)
        self.assertEqual(tokenizer.next.value, 20)

        tokenizer.select_next() # tokenizer.next = *

        self.assertIsInstance(tokenizer.next, MultToken)

        tokenizer.select_next() # tokenizer.next = 3

        self.assertIsInstance(tokenizer.next, NumericToken)
        self.assertEqual(tokenizer.next.value, 3)

        tokenizer.select_next() # tokenizer.next = \0

        self.assertIsInstance(tokenizer.next, EOFToken)


if __name__ == "__main__":
    unittest.main()
