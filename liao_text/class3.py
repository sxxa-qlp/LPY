class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def get_grade(self):
		if self.__score>=90:
			return 'A'
		if self.__score>=60:
			return 'B'
		else:
			return 'C'

	def print_score(self):
		print('%s:%s,LEVEL %s'%(self.__name,self.__score,self.get_grade()))

	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score

	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simth',99)
jack = Student('Jack Disney',43)

jack.print_score()
	







