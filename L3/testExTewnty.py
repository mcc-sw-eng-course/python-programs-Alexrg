import unittest
from exTwenty import cpuTime, clockTime

class TestClocks(unittest.TestCase):
    def test_clock_greater(self):
        self.assertGreater(clockTime(),cpuTime())

    def test_cpu_smaller(self):
        self.assertLess(cpuTime(),clockTime())

    def test_clock_not_smaller(self):
        self.assertFalse(cpuTime()>clockTime())

    def test_cpu_is_smaller(self):
        self.assertTrue(cpuTime()<clockTime())

    def test_cpu_and_clock_are_not_equal(self):
        self.assertIsNot(cpuTime(),clockTime())

if __name__ == '__main__':
    unittest.main()
