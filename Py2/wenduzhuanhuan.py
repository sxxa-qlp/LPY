tempstr = input()
#注意判断条件的写法
if tempstr[0] in ['F','f']:
	#注意eval将字符转换成数字
	C = (eval(tempstr[1:]) - 32)/1.8
	#注意format输出格式
	print('C{:.2f}'.format(C))
else:
	F = (eval(tempstr[1:])) * 1.8 + 32
	print('F{:.2f}'.format(F))