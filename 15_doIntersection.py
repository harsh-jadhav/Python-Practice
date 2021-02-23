
a = [1, 2, 3, 4, 5]
b = [85, 2, 76, 10, 11, 23, 29, 30]

def Intersect_A_B(a,b):
	"""
	This function returns the union of the two arrays
	"""
	m = len(a)
	n = len(b)
	inter = []

	if m>n:
		inter = [i for i in b if i in a]
	else:
		inter = [i for i in a if i in b]

	print(sorted(inter))

# Intersect_A_B(a,b)



def print_intersection(a, b):
	m = len(a)
	n = len(b)

	i, j = 0, 0

	while i<m and j<n:
		if a[i]<b[j]:
			i+=1
		elif b[j]<a[i]:
			j+=1
		else:
			print(b[j])
			i+=1
			j+=1

# a = [1, 2, 4, 5, 6] 
# b = [2, 3, 5, 7] 
print_intersection(a, b)