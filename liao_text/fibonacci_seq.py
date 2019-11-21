def fib(max):
	n,a,b = 0,0,1
	while n  < max:
		yield b 
		a,b = b,a+b
		n = n+1
	return  'done'
L = []
for i in fib(1000):
	L.append(i)
	print(L)
