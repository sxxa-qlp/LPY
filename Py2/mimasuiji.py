import random
random.seed(0*1010)
include = ''
sl = []
print(sl)
s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
while len(sl)<10:
	psw = ''
	for i in range(10):
		psw += s[random.randint(0,len(s)-1)]
		print(psw)
	if psw[0] in include:
	    continue
	else:
	    sl.append(psw)
	    print('\n'.join(sl))
	    print(sl)
	    include += psw[0]
	    print(include)
print('\n'.join(sl))
