# Medium Accuracy: 46.66% Submissions: 23922 Points: 4
# Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Example 1:

# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.


def kth_smallest_element(arr, k):
	# sort the array in ascending order
	arr = sorting(arr) # we can also use built in sorted() function
	# return the value at desired index
	return arr[k-1]

def  sorting(arr):
	"""This is a custom sort function"""
	# arr = [-15, -26, 15, 1, 23, -64, 23, 76]
	# create a new list 
	new_list = []
	# until the arr is not empty (empty arrays are False and filled arrays are True)
	while arr:
		# set the first value of array as minimum(smaller value)
	    min_ = arr[0] 
	    # the for each element in array check if the element is less than the minimum value
	    for x in arr: 
	        if x < min_:
	            # if element is smaller then set it as minumum
	            min_ = x
	    # and now append that smallest number to the 
	    new_list.append(min_)
	    arr.remove(min_)    

	return new_list

array =  [int(i) for i  in "7 10 4 3 20 15".split()]

print(kth_smallest_element(array, 3))