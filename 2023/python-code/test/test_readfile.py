import sys, os
import unittest

sys.path.append("..")
from funcs.readfile import ReadFileObject

class Tests(unittest.TestCase):
    def test_readfile(self):
        filepath = os.path.join(os.path.dirname(__file__), 'test_inputs.txt')
        isSuccess, lines = ReadFileObject().get_lines_from_file(filepath)
        self.assertEqual(True, isSuccess, "File reading not successful!")
        self.assertEqual(100, len(lines), "File should contain 100 lines!")


if __name__ == "__main__":
    unittest.main()