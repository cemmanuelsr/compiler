import unittest

from processes.PrePro import PrePro


class TestPrePro(unittest.TestCase):

    def test_pre_process(self):
        code = "1 + 2*3  //some comment here"
        cleaned_code = "1 + 2*3"
        self.assertEqual(cleaned_code, PrePro.pre_process(code))


if __name__ == "__main__":
    unittest.main()
