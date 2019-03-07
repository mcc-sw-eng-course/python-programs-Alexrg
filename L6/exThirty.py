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
	call_quick_sort_function = quick_sort(data, call_pivot_function, list_length)
	end_time = datetime.time(datetime.now())

	print("Start time: {}".format(start_time))
	print("End time: {}".format(end_time))

	return  start_time, end_time

time_performance = get_time_consumed(list)
print("Time consumed in the function: {}".format(time_performance))

