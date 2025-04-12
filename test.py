import unittest
from main import is_even, add

class TestCLITool(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

if __name__ == "__main__":
    unittest.main()
