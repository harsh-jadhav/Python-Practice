b = [1, 2, 3, 4, 5]
a = [85, 2, 76, 10, 11, 23, 29, 30]

def doUnion(a, b):
	"""
	This function returns the union of the two arrays
	"""
	# m = len(a)
	# n = len(b)
	# union = []
	
	union = list(sorted(set(a).union(set(b))))
	return union


print(doUnion(a, b))


def Union_A_B(a,b):
	"""
	This function returns the union of the two arrays
	"""
	m = len(a)
	n = len(b)

	if m>n:
		union = a + [i for i in b if i not in a]
	else:
		print("b greater")
		union = b + [i for i in a if i not in b]

	print(sorted(union))

Union_A_B(a,b)
