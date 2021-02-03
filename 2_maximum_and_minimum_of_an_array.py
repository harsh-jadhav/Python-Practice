import datetime

arr = [9,2,22,13,25,17,19,95]
# using custom linear search
def min_max_linear_search(array):
	# get the length of the input array
	n = len(array)
	# if array has only one element return same number as min and max both
	if n==1:
		return array[0], array[0]
	# set the intial values for  min and max using first two elements of array
	if array[0]>array[1]:
		maximum, minimum = array[0], array[1]
	else:
		maximum, minimum = array[1], array[0]
	# iterate over the array from 3rd element
	for i in arr[2:]:
		# check if the number is greater than previous value of max and set it to current max value
		if i > maximum:
			maximum=i
		# check if the number is less than previous value of min and set it to current min value
		if i < minimum:
			minimum=i
	# finally return the max and min value
	return maximum, minimum

max_value, min_value = min_max_linear_search(arr)
startTime = datetime.datetime.now()
print("max,min: linear search: ", min_max_linear_search(arr))
print("Time taken:")
print(datetime.datetime.now() - startTime)

# Using  python default function
arr = [9,2,22,13,25,17,19,95]

def min_max_python(array):
	
	return max(array), min(array)


startTime = datetime.datetime.now()
print("max,min: python way: ", min_max_python(arr))
print("Time taken:")
print(datetime.datetime.now() - startTime)