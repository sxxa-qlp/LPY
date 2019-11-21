from math import pi
r = input('enter redus')
r = eval(r)
s = 4*pi*pow(r, 2)
v = 4/3*(pi*pow(r, 3))
print('{0:.2f} {1:.2f}'.format(s,v))