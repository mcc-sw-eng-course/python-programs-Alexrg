from datetime import date, time, datetime
from exTwentynine import quick_sort, choose_pivot_number

"""
Implement the method
- get_performance_data()
This method returns the performance data associated to the last sorting execution
[Number of Records Sorted, TimeConsumed, StartTime, EndTime]
"""
list = [0, 4, 5, 103, 98, 35, 86, 7, 1, 1, 100, 3, 0, 45, 5, 3, 19, 35, 86, 7, 1, 1, 100, 3]
list_length = len(list)

def get_time_consumed(data):
	start_time = datetime.time(datetime.now())
	call_pivot_function = choose_pivot_number(list)
	call_quick_sort_function = quick_sort(data, call_pivot_function, list_length-2)
	end_time = datetime.time(datetime.now())

	start_time = start_time.strftime("%H:%M:%S")
	end_time = end_time.strftime("%H:%M:%S")

	#time_consumed = int(end_time) - int(start_time)

	return  start_time, end_time
	#return  time_consumed

def get_records_sorted(list):
	records_sorted = 0
	for i in list:
		records_sorted  += 1

	return records_sorted

time_performance = get_time_consumed(list)

start_time = time_performance[0]
end_time = time_performance[1]

print("Start time: {} - End time: {}".format(start_time,end_time))
#print("Time consumed in the function: {}".format(time_performance))

records_counted = get_records_sorted(list)
print("Records counted: {}".format(records_counted))