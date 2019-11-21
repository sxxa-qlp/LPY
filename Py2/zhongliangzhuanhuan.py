# WeightConvert
# 1千克(kg, 公斤)=2斤
TempStr = input("请输入带有单位的重量值(10千克或10斤)：")
if TempStr[-1] == '斤':
	#注意切片操作倒着切还需正着数
    out = eval(TempStr[:-1])/2
    print('转换后的重量为：{}千克'.format(out))
# 判断是否属于斤，并执行转换
else:
    out = eval(TempStr[:-2])*2
    print('转换后的重量为：{}斤'.format(out))

# 输入错误时，提示信息
