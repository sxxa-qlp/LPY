from scipy import integrate
import numpy as np
import math
#定义数学函数
def f(t):
	return pow(math.cos(t)+4*math.sin(2*t)+5,0.5)

#梯形法
def trape(f,a,b,n=100):
	f = np.vectorize(f)
	h = float(b-a)/n
	arr = f(np.linspace(a,b,n+1))
	print(arr)
	return (h/2)*(2*arr.sum()-arr[0]-arr[-1])

a, b = 0 ,2*math.pi
print(trape(f,a,b))
