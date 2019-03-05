"""
Implement the method:
- execute_heap_sort()
This methods sorts the data contained in the file specified. Define
custom exceptions or error codes for situations where there may be special errors.
"""

#list = [1,2,3,4,5,6,7,8]
list = [3,5,3,7,8,6]
length = len(list)
n = length - 1
new_list = []


def heapTree(list, n, i):
	largest_index = list[n]
	l = i
	r = i - 1    
	left = list[l]
	rigth = list[r]
	
	return left, rigth

def order_elements(elements):
	ordered_list = []
	if (elements[0]>elements[1]):
		ordered_list.append(elements[0])
		ordered_list.append(elements[1])
	else:
		ordered_list.append(elements[1])
		ordered_list.append(elements[0])
	
	return ordered_list

# Build a maxheap. 
for i in range(n, -1, -1): 
	tree = heapTree(list, n, i)
	order = max(order_elements(tree))
	new_list.append(order)
print(list)
print(new_list)