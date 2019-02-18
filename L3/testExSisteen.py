import unittest
from exSixteen import upper

class TestUpper(unittest.TestCase):
    def test_true_one(self):
        self.assertTrue(upper(.13),1)

    def test_true_two(self):
        self.assertTrue(upper(3.45), 4)

    def test_equal(self):
        self.assertEqual(upper(.13),1,1)

if __name__ == '__main__':
    unittest.main()
