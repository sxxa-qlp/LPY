class Student(object):
	# 属性是常量的直接赋值，不需导入参数
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def get_grade(self):
		if self.score>=90:
			return 'A'
		if self.score>=60:
			return 'B'
		else:
			return 'C'
#输出调用方法（函数）
	def print_score(self):
		print('%s:%s,LEVEL %s'%(self.name,self.score,self.get_grade()))


bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simth',99)
#对象调用方法（函数）
bart.print_score()
lisa.print_score()


