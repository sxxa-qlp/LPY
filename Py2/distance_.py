str = input('enter 4 num...')
sls = str.split()
a = eval(sls[0])
b = eval(sls[1])
c = eval(sls[2])
d = eval(sls[3])
dis = pow(pow(a - c ,2)+ pow(b - d, 2), 0.5)
print('{:.2f}'.format(dis))i