class Student(object):
	__slots__ = ('name','age')

def set_name(self,name):
	self.name = name 

s1 = Student()
s2 = Student()
s3 = Student()

Student.set_name = set_name
s1.set_name('s1')
s2.set_name('s2')
print(s1.name)
print(s2.name)

s1.age = 23
print(s1.age)

#子类不受限，若子类有__slots__则需同时满足自己和父类
class GraduateStudent(Student):

	__slots__ = ('name','age','gender')

	# def __init__(self):
	# 	pass
		

g = GraduateStudent()
g.age = 38
g.name= 233
g.gender = 'male'
print(g.age,g.name,g.gender)