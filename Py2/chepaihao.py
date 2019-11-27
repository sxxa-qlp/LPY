with open('car_data.txt',encoding = 'gbk') as f :
    LS = f.readlines()
O = [0,0,0,0]
for i in LS :
    x = i.split(',')
    #注意列表x中的元素
    if x [0] == '2:00' and eval(x[2]) >= 31.30:
        for i in range(4):
            O[i] = x[i]
        #注意print位置 每生成一个list后输出
        #注意print后不换行'\n'---->replace with end = ''
        print('时间:{:} 车牌:{:} 北纬:{:} 东经:{:}'.format(O[0],O[1],O[2],O[3]),end = '')
    else:
        None