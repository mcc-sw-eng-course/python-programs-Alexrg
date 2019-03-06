"""
Write a function that computes the standard deviation for a set of numbers coming from a
list. Do notuse anymath module, compute the algorithm
"""
import math

student_grades = [10, 8, 7, 6, 5, 10, 6, 7]
n = len(student_grades)

def sum_elements(data):
	sum = 0
	
	for x in data:
		sum = sum + x

	return sum

def calculate_mean(data, n):
    sum = sum_elements(data)
    avg = round((sum /n),2)
    
    return avg

def calculate_deviations(data, mean, n):	
	data_deviation = 0
	variance = 0

	for x in data:
		data_deviation += math.pow(x - mean,2)

	variance = data_deviation/n
	std_deviation = round(math.sqrt(variance),2)

	return std_deviation

student_avg = calculate_mean(student_grades, n)
student_deviations = calculate_deviations(student_grades, student_avg, n)

print("The student's average: {}".format(student_avg))
print("The student's deviation: {}".format(student_deviations))