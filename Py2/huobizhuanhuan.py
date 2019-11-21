temp = input()
#注意判断条件字符的始末位置
if temp[0:3] in ['usd','USD']:
	RMB = eval(temp[3:])*6.78
	print('RMB{:.2f}'.format(RMB))
else:
	USD = eval(temp[3:])/6.78
	print('USD{:.2f}'.format(USD))