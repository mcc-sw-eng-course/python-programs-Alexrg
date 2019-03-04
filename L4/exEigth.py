import statistics
import random

data = [6, 7, 2, 3, 8, 4, 5, 6, 6, 7, 1, 3]

#Print data to the user
print(data)

#1. Sample mean function
def mean(data):
    sum = 0
    for x in data:
        sum = sum + x
    avg = round((sum / len(data)),2)
    return avg

#2. Standard deviation function
def standardDeviation(data):
    std_dev = round((statistics.stdev(data)),2)
    return std_dev

def median(data):
    ordered_data = sorted(data)
    data_length = len(ordered_data)
    med = 0
    if (data_length % 2 == 0):
        position = int(data_length / 2)
        med = (data[position-1]+data[position])/2
    elif (data_length % 2 != 0):
        position = int((data_length - 1)/2)
        med = data[position]
    return med, position

def quartil(quartil,data):
    ordered_data = sorted(data)
    if (quartil == 1):
        return 1
    elif (quartil == 2):
        chosen_quartil = median(data)
        return chosen_quartil[0]
    elif (quartil == 3):
        return 3

def percentil(percentil,data):
    value = int((percentil / 100) * 10)
    percentil_value = data[value]
    return percentil_value

#Print the sample mean results
calculate_mean = mean(data)
print("The mean: {}".format(calculate_mean))

#Print the standard deviation results
calculate_std_dev = standardDeviation(data)
print("The standard deviation: {}".format(calculate_std_dev))

#Print the median results
calculate_median = median(data)
print("The median: {}".format(calculate_median[0]))

#Print the quartil
pick_quartil = random.randint(1,3)
calculate_chosen_quartil = quartil(pick_quartil,data)
print("The {} quartil: {}".format(pick_quartil, calculate_chosen_quartil))

#Print the quartil
pick_percentil = random.randint(1,100)
calculate_chosen_percentil = percentil(pick_percentil,data)
print("The {} percentil: {}".format(pick_percentil, calculate_chosen_percentil))