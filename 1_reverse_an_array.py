# Given an array (or string), the task is to reverse the array/string.
# Examples : 
 

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

# 1. Iterative way : # Time Complexity : O(n)

arr = [5,4,3,2,1]
n = len(arr)
start = 0
end = n-1

for i in range(n):
	if start<end:	
		arr[start], arr[end] = arr[end], arr[start]
		start = start + 1
		end = end - 1

print('Iterative Way: ',arr)

# 2. Recursive Way : # Time Complexity : O(n)

arr = [5,4,3,2,1]
start = 0
end = len(arr) - 1

def reverse_it(array, start, end):
	if start >= end:
		return
	array[start], array[end] = array[end], array[start]
	reverse_it(array,start+1,end-1)


reverse_it(arr, start, end)

print("Recursive Way: ",arr)


# 3. python slicing way:

arr = [5,4,3,2,1]

print("Slicing way: ", arr[::-1])