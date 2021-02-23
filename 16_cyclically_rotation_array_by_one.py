a = [85, 2, 76, 10, 11, 23, 29, 30]

def rotateByOne(array):
	x = array.pop()
	array[0]=x
	return array

print(rotateByOne(a))


for i in range(len(a) - 1, 0, -1): 
	print(i)
	# a[i] = a[i - 1]

print(a)