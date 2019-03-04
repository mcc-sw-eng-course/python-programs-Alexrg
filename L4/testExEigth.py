import unittest
import exEigth

class TestExEight(unittest.TestCase):
	"""
	Create tests
	"""
	def equal_mean(self):
		dataTest = [1,2,3,4,5,6]
		data = [6, 7, 2, 3, 8, 4, 5, 6, 6, 7, 1, 3]
		meanTest = mean(dataTest)
		mean = mean(data)
		self.assertNotEqual(meanTest, mean)

if __name__ == '__main__':
    unittest.main()
