n = 300


def maxDivide(a, b):
	"""
	This function performs the division of numbner 'a' 
	by number 'b' till it is completely divisible by 'b'
	and return that the final value

	"""
	while a%b == 0:
		# print("okay in: ",a)
		a = a/b
	return a

def isUgly(n):
	"""
	Here we will perform division by 2, 3 and 5 using 
	maxDivide function
	if final 'n' has 1 value then it is an ugly number otherwise 
	it is not an ugnly number
	"""
	n = maxDivide(n, 2)
	n = maxDivide(n, 3)
	n = maxDivide(n, 5)

	return 1 if n==1 else 0

def getNthUgly(nt):
	""" 
	This function finds the nth ugly number 
	"""
	# we will initialize the number from 1 because 1 is conventionally considered 
	# as ugly number
	i = 1
	# we have 1 as ugly number hence we will intialize count as 1
	count = 1
	# now until count is less than our desired nth value
	# increment the number i by 1, and check if the i is an ugly number
	while nt > count:
		# increment the value of i by 1
		i+=1
		# check if "i" is an Ugly number
		if isUgly(i):
			# if "i" is an ugly number then increment the count by 1
			count+=1
	# finally return the value of "i" as it will be our nth ugly number
	return i

print("Simple programming way: ",getNthUgly(150))
# isUgly(n)
# print(maxDivide(n, 2))
# print()

# print(maxDivide(n, 3))
# print()

# print(maxDivide(n, 5))


# by using dynamic programming
n = 150
def ugly_dynamic(n):

	# create an arraay with all zeros
	arr = [0]*n
	# set the first element of the array as 1
	arr[0] = 1
	# intialize the values of indices of multiple of 2,3,5 to 0
	i2 = 0
	i3 = 0
	i5 = 0
	# set the first multiples of 2,3,5 that will be 2,3, and 5 resp
	nm2 = arr[i2]*2
	nm3 = arr[i3]*3
	nm5 = arr[i5]*5
	# now iiterate over the number of elements from 1
	for x in range(1, n):
		# set the elemet at x as minimum value of all the multiple
		# of 2,3,5
		arr[x] = min(nm2, nm3, nm5)
		# check if the element is next multiple of 2
		if arr[x] == nm2:
			# increment the index i2 byy one
			i2 += 1
			# set next multiple of 2 as below
			nm2 = arr[i2]*2

		if arr[x] == nm3:
			# increment the index i3 byy one
			i3 += 1
			# set next multiple of 3 as below
			nm3 = arr[i3]*3

		if arr[x] == nm5:
			# increment the index i5 byy one
			i5 += 1
			# set next multiple of 5 as below
			nm5 = arr[i5]*5
		
	return arr[-1]

print("Dynamic programming way: ",ugly_dynamic(n))