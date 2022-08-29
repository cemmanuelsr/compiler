import unittest

from processes.PrePro import PrePro


class TestPrePro(unittest.TestCase):

    def test_clean_comments(self):
        code = "1 + 2*3  //some comment here"
        cleaned_code = "1 + 2*3"
        self.assertEqual(cleaned_code, PrePro._clean_comments(code))

    def test_clean_spaces(self):
        code = "1    + 2  *3"
        cleaned_code = "1+2*3"
        self.assertEqual(cleaned_code, PrePro._clean_spaces(code))

    def test_pre_process(self):
        code = "1    + 2  *3  // some comment here"
        cleaned_code = "1+2*3"
        self.assertEqual(cleaned_code, PrePro.pre_process(code))


if __name__ == "__main__":
    unittest.main()
