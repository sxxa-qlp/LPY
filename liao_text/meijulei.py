from enum import Enum
class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):
	def __init__(self, name, gender):
		self.name = name 
		if gender in Gender:
			self.gender = gender
		else:
			raise ValueError('Invalid gender')

bart = Student('Bart', Gender.Male)
print(bart.gender)