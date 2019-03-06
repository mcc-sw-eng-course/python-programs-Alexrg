import random

"""
Implement the method
- execute_quick_sort()
This methods sorts the data contained in the file specified. Define custom exceptions or
error codes for situations where there may be special errors
"""

# La lista que se odernará
list = [0, 4, 8, 3, 9, 5, 6, 7, 1, 1]
list_length = len(list)
new_list = []
print(list)

# 1. Elegir un elemento del arreglo de elementos a ordenar, al que llamaremos pivote.
pivot_index = random.randint(0, list_length-1)
pivot_number = list[pivot_index]

# 2. Resituar los demás elementos de la lista a cada lado del pivote, de manera que a un
# lado queden todos los menores que él, y al otro los mayores. Los elementos iguales al
# pivote pueden ser colocados tanto a su derecha como a su izquierda, dependiendo de la
# implementación deseada. En este momento, el pivote ocupa exactamente el lugar que le
# corresponderá en la lista ordenada
pivot_left = []
pivot_rigth = []
pivot = []
for i in range(0, list_length-1):
	if list[i] < pivot_number:
		pivot_left.append(list[i])
	elif pivot_number < list[i]:
		pivot_rigth.append(list[i])
	elif pivot_number == list[i]:
		pivot.append(list[i])

new_list.append(pivot_left)
new_list.append(pivot)
new_list.append(pivot_rigth)

print(new_list)

