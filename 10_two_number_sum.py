A = [3, 5, -4, 8, 11, 1, -1, 6]
C = 10

#
temp = []
# for each number in an array
for i in range(len(A)-1):
	# for each next number of the number i
	for j in range(i+1, len(A)):
		# check if the sum equal to target sum
		if A[i]+A[j]==C:
			# if yes then we have our two numbers 
			temp = [A[i],A[j]]

print(temp)

# create a set or a dictionary to store checked numbers
se = set()
t = []
# for each number in array
for i in A:
	# find the difference between target sum and the number
	y = C-i
	# if the difference is present in our set
	if y in se:
		# then we have the two numbers which adds up to target sum
		t=[y, i]
	# otherwise add the checked number to the set()
	else:
		se.add(i)

print(t)

def twoNumberSum(array, Sum):
	# first sort the array 
	s_arr = sorted(array)
	# set the left index to 0
	L = 0
	# set the right index to length of array - 1
	R = len(array)-1
	# then we will run a while loop untill 
	# the left value is less than Right value
	while L<R:
		# if the sum of the left and right element is equal to 
		# target sum then return those elements as list
		l_r_sum = s_arr[L] + s_arr[R]
		if  == Sum:
			return [s_arr[L], s_arr[R]]
		# if the sum is less than target sum
		elif l_r_sum < Sum:
			# increment the left value by one and move it to right
			L = L + 1
		# if the sum is greater than target sumn
		elif l_r_sum > Sum:
			# decrement the right value by 1 and move it to the left
			R = R - 1
	# otherwise just return empty list 
	return []

print(twoNumberSum(A, 20))