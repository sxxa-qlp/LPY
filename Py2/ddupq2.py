# DayDayUP_NewQ2
#建立函数
#for 循环里加 if 判断-------> for-if 形式
#返回函数值
def dayUP():
    up = 1
    #判别周末
    for i in range(365):
    	if i % 7 in [0,6]:
	    	up *= (1-0.001)
    	else:
    		up *= (1+0.01)
    return up
print("天天向上的力量为：{:.2f}。".format(dayUP()))