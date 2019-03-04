"""
Ask the user for a number. Depending on whether the number is even or
odd, print out an appropriate message to the user. Hint: how does an even /
odd number react differently when divided by 2?
If the number is a multiple of 4, print
out a different message.
Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that to the
user. If not, print a different appropriate message.
"""

def oneNumber():
	input_number = int(input('Enter a number:'))
	
	if (input_number % 2 == 0):
		message = "The number is divisible by two"

		if (input_number % 4 == 0):
			message = message + " and by four"

	return message

def twoNumbers():
	num = int(input("Enter another number: "))
	check =  int(input("Enter the divider of that number: "))

	if (num % check == 0):
		message = "The first number is divisible by the second one"
	else:
		message = "The first number is not divisible by the second one"
	return message

result_one = oneNumber()
print(result_one)

result_two = twoNumbers()
print(result_two)