class Student(object):
	@property 
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be integer!')
		if value > 100 or value < 0:
			raise ValueError('score must between 0-100')
		self._score = value

s = Student()
s.score = 2323
print(s.score)