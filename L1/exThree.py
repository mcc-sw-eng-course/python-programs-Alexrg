"""
Write a program (function!) that takes a list and returns a new list that contains all the
elements of the firstlist minus all the duplicates.Write two different functions to do this
one using a loop and constructing a list, and another using sets.
"""

def eliminate_duplicates(list):
	unique_elements = []
	
	for element in list:
		if element not in unique_elements:
			unique_elements.append(element)
	
	return unique_elements

list = [1, 2, 3, 2, 2, 5, 6, 8, 1]
print("Your list: {}".format(list))

unique_elements = eliminate_duplicates(list)
print("Your list without duplicates: {}".format(unique_elements))