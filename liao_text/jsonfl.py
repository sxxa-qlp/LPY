import json
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
s = Student('Bob', 23, 98)
#_____student2dict_____
# def student2dict(std):
# 	return{
# 		'name':std.name,
# 		'age':std.age,
# 		'score':std.score
# 	}
def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

json_str = '{'age':39,'score':32,'name':23}'
print(json.loads(json_str,object_hook=dict2student))














print(json.dumps(s))