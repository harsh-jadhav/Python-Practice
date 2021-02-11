# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.
# Given an array of size N containing only 0s, 1s, and 2s; 
# sort the array in ascending order.


# Constraints:
# 1 <= N <= 10^5
# 0 <= A[i] <= 2
import numpy as np
def sort012(arr,n):
	"""pythonic solution"""
	return np.sort(arr)

N = 5
array = [0, 2, 1, 2, 0]

print("Pythonic Way: ",sort012(array, N))

def counting_sort012(arr, n):
	zeros = arr.count(0)
	ones = arr.count(1)
	twos = arr.count(2)
	return [0]*zeros + [1]*ones + [2]*twos

print("Counting Sort: ", counting_sort(array, N))