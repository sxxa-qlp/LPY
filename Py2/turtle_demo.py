import turtle as t
#拿起画笔
t.pu()
#向左250
t.fd(-250)
#落下画笔
t.pd()
#画笔尺寸
t.pensize(25)
#颜色
c = ['red','purple','orange','green']
#设置头部角度
t.seth(-40)
for i in range(4):
	t.pencolor(c[i])
	t.circle(40,80)
	t.circle(-40,80)
t.pencolor('yellow')
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)
t.done()