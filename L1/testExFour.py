import unittest
from exFour import sum_elements, calculate_mean

student_grades = [10, 8, 7, 6, 5, 10, 6, 7]
n = len(student_grades)
sum_student_grades = 10 + 8 + 7 + 6 + 5 + 10 + 6 + 7
mean_student_grades = round((sum_student_grades / n),2)


class TestStandardDeviation(unittest.TestCase):
    def test_sum_equal(self):
    	self.assertEqual(sum_elements(student_grades),sum_student_grades)

    def test_mean_equal(self):
    	self.assertEqual(calculate_mean(student_grades, n), mean_student_grades)

if __name__ == '__main__':
    unittest.main()
