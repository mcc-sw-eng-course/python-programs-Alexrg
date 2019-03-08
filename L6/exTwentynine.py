import random

"""
Implement the method
- execute_quick_sort()
This methods sorts the data contained in the file specified. Define custom exceptions or
error codes for situations where there may be special errors
"""
# Crear una lista con números y tamaño aleatorio
def create_list():
	list = []
	list_length = random.randint(0, 200)
	for i in range(0,list_length):
		list.append(random.randint(0, 100))
	print (list)
	return list

list_two = create_list()
list_two_length = len(list_two)

# 1. Elegir un elemento del arreglo de elementos a ordenar, al que llamaremos pivote.
def choose_pivot_number(list, length):
	pivot_index = random.randint(0, length)
	pivot_number = list[pivot_index]
	return pivot_number

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


pivot_number = choose_pivot_number(list_two, list_two_length)

sort = quick_sort(list_two, list_two_length, pivot_number)
print(sort)
# 3. Repetir este proceso de forma recursiva para cada sublista mientras éstas contengan más
# de un elemento. Una vez terminado este proceso todos los elementos estarán ordenados.
if (sort == list_two.sort()):
	print("La lista ya está ordenada")
else:
	sort = quick_sort(list_two, list_two_length, pivot_number)
	print(sort)

