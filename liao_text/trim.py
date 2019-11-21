class Student(object):
	def __init__(self,name,gender):
		self.name = name
		self.__gender = gender 

	def get_gender(self):
		return self.__gender
	def set_gender(self,gender):
		if gender in ('male','female','x'):
			self.__gender = gender 
		else:
			raise ValueError('bad value')

	def get_inf(self):
		print('%s:%s'%(self.name,self.__gender))

machael = Student('Machael Jordan', 'male')
print(machael.get_gender())
machael.set_gender('x')
print(machael.name,':',machael.get_gender())




