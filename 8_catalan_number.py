
def catalan(n):
	if n==1 or n==0:
		return 1
	cn = 0
	for i in range(n):
		# print(catalan(i), catalan(n-i-1))
		cn += catalan(i)*catalan(n-i-1)
	return cn

print(catalan(9))


def catalanDynamic(n):
	cat = [0]*(n+1)
	cat[0] = 1
	cat[1] = 1
	for i in  range(2, n+1):
		for j in range(i):
			cat[i] += cat[j]*cat[i-j-1]
	return cat[n]

print(catalanDynamic(9))