def findMinAndMax(L):
	if L != []:
		(min,max) = (L[0],L[0])
		for i in L:
			if max<i:
				max = i
			if min>i:
				min = i
		return(min,max)
	else:
		return(None,None)
print(findMinAndMax([4,5,6,7,7,9,66]))