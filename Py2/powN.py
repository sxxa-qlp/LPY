N = float(input())
#先算前5个
for i in range(5):
	#注意end为空格
	print(pow(N, i),end = ' ')
print(pow(N, 5))