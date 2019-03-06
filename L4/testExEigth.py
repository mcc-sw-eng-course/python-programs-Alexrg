import unittest
from exEigth import mean

class TestExEight(unittest.TestCase):
	"""
	Create tests
	"""
	
	dataTest = [1, 2, 3, 4, 5, 6]
	data = [6, 7, 2, 3, 8, 4, 5, 6, 6, 7, 1, 3]

	def equal_mean(self):
		
		meanTest = mean(dataTest)
		mean = mean(data)
		self.assertNotEqual(meanTest, mean)

if __name__ == '__main__':
    unittest.main()
