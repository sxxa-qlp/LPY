L1 = ['HELLO','APPEN',23,'BIg']
#第一种方法
L = [i.lower() for i in L1 if isinstance(i,str)]
print(L)

#第二种方法
L2 = []
for i in L1:
	if isinstance(i , str):
		n = i.lower()
		L2.append(n)
	else:
		pass
print(L2)