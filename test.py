import unittest
from main import is_even

class TestCLITool(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

if __name__ == "__main__":
    unittest.main()
