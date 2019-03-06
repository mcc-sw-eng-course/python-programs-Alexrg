"""
Write a functionthat receives as parameters how many Fibonnaci numbers to generate and
then generates them. Take this opportunity to think about 0,0.5,1,3,8,2000,450000,-1,p,[]
how you can use functions. Make sure to ask the user to enter the number of numbers
in the sequence to generate.(Hint: The Fibonnaci sequenceis a sequence of numbers where
the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...)
"""
# Fibonacci numbers to generate
fibonacci_numbers = 8
first_number = 1

# Generate the array
def generate_fibonaci(fibonacci_numbers, first_number):
	fibonacci = [first_number]
	fibonacci.append(first_number)
	sum = 0

	for i in range(2, fibonacci_numbers):
		sum = fibonacci[i-1]+fibonacci[i-2]
		fibonacci.append(sum)
		sum = 0

	return fibonacci

fibonacci = generate_fibonaci(fibonacci_numbers, first_number)
print(fibonacci)