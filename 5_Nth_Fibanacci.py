def fibancci(n):
	fib = [0,1]

	for i in range(2, n+1):
		fib.append(fib[i-1] + fib[i-2])
	return fib[n]

print(fibancci(10))

def fibancciR(n):
	fib = [0,1]
	if n==0:
		return 0
	elif n==1:
		return 1
	return fibancciR(n-1) + fibancciR(n-2)

print(fibancciR(10))