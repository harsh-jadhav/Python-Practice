arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]


def move_negatives_ahead(arr):
	l = [i for i in arr if i<0]
	r = [i for i in arr if i>0]
	return l+r

print(move_negatives_ahead(arr))


def move_negatives(arr):
	# intialize an index for storing number track
	j = 0
	# for each element in an array 
	for i in range(len(arr)):
		# check if the element is less than 0
		if arr[i]<0:
			# if less than zero i.e. negative number 
			# then save it as current negative number
			current = arr[i]
			# swap that number by previous non-negative number
			arr[i] = arr[j]
			# set the current 
			arr[j] = current
			# increment the value of j by 1
			j += 1
		# print(i,arr)
		# print()
	return arr

print(move_negatives(arr))