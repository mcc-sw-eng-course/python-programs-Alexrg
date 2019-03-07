import random

"""
Implement the method
- execute_quick_sort()
This methods sorts the data contained in the file specified. Define custom exceptions or
error codes for situations where there may be special errors
"""

# La lista que se odernará
list = [0, 4, 5, 3, 9, 35, 6, 7, 1, 1, 100, 3]
list_length = len(list)
new_list = []
print(list)

# 1. Elegir un elemento del arreglo de elementos a ordenar, al que llamaremos pivote.
pivot_index = random.randint(0, list_length-1)
pivot_number = list[pivot_index]
print("pivot: {}".format(pivot_number))

# 2. Resituar los demás elementos de la lista a cada lado del pivote, de manera que a un
# lado queden todos los menores que él, y al otro los mayores. Los elementos iguales al
# pivote pueden ser colocados tanto a su derecha como a su izquierda, dependiendo de la
# implementación deseada. En este momento, el pivote ocupa exactamente el lugar que le
# corresponderá en la lista ordenada
def quick_sort(list, list_length, pivot_number):
	pivot_left = []
	pivot_rigth = []
	pivot_list = []

	new_list = []

	for i in range(0, list_length):
		if list[i] < pivot_number:
			pivot_left.append(list[i])
		elif pivot_number < list[i]:
			pivot_rigth.append(list[i])
		elif pivot_number == list[i]:
			pivot_list.append(list[i])

	new_list = pivot_left + pivot_list + pivot_rigth
	
	return new_list

sort = quick_sort(list, list_length, pivot_number)

# 3. Repetir este proceso de forma recursiva para cada sublista mientras éstas contengan más
# de un elemento. Una vez terminado este proceso todos los elementos estarán ordenados.
if (new_list == list.sort()):
	print("La lista ya está ordenada")
else:
	sort = quick_sort(list, list_length, pivot_number)
	print(sort)

