# date = input('xxxx-xx-xx')
# y = int(date[0:4])
# m = int(date[5:7])
# d = int(date[8:])
y = int(input())
m = int(input())
d = int(input())
#世纪闰年
if y % 100 == 0 :
	if y % 400 == 0:
		ly = True
	else:
		ly = False
#一般闰年
if y % 4 == 0 :
	ly = True
else:
	ly = False

if ly == True :
	ms = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
	ms = [31,28,31,30,31,30,31,31,30,31,30,31]

days = 0
day = 0
#注意print位置
for i in range(1,13):
	if i == m:
		for j in range(i-1):
			days = days + ms[j]
		day = days + d
print(day)





