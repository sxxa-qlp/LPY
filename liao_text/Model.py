class Field(object):
	def __init__(self, name, column_type):
		self.name = name 
		self.column_type = column_type

	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name, 'bigint')

class ModeMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name=='Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model: %s'%name)
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==>%s'%(k,v))
				mappings[k] = v
		for k in mappings.keys()；














			