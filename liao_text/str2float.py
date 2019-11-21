from functools import reduce
def str2float(s):
	#定位小数点
	p = s.index('.')
	s1 = s[:p]
	s2 = s[p+1:]
	#字符串转数字的字典
	digits = {'0':0,'1':1,'2':2,'3':3, '4':4 , '5':5, '6':6 , '7':7, '8':8, '9':9}
	#reduce调用
	def fn(x,y):
		return 10*x+ y 
	#map调用
	def char2num(s):
		return digits[s]
	return reduce(fn,map(char2num,s1))  + reduce(fn,map(char2num,s2)) * (10**(0-3))
print(str2float('233454.234'))