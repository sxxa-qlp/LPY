with open('BP.txt',encoding = 'gbk') as f :
    LS = f.readlines()
del LS[0]
O = [0,0,0]
for i in LS :
    x = i.split(',')
    for i in range(3):
    	#计算前注意数据类型的转换
        O[i] += int(x[i+1])
for i in range(3):
    O[i] = O[i] / len(LS)
print('收缩压平均值：{:.3f},舒张压平均值：{:.3f},心率平均值：{:.3f}'.format(O[0],O[1],O[2]))