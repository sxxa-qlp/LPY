# 输入元素创建列表，列表中的元素至少包含一个数值型（int或者float）数据，
# 列表元素个数也要求通过input()函数输入，长度不限。
# 要求：统计列表中数值数据的个数，并输出。
num = eval(input())
Ls = []
for i in range(num):
    a = input()
    #注意使用isdigit函数判断
    #是否是数字并转成int
    if a.isdigit():
        a = int(a)
        Ls.append(a)
    else:
        Ls.append(a)
d = 0
for i in Ls:
    if isinstance(i, int) or isinstance(i, float):
        d +=1
    else:
        d = 0
print('所创建的列表为{:}列表中一共有{:}个数值数据'.format(Ls,d))