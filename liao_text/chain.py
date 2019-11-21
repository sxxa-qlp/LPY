class Chain(object):
	def __init__ (self,path= ''):
		self._path = path
#动态链式调用
	def __getattr__(self,path):
		return Chain('%s/%s'%(self._path,path))
#用print显示时调用该函数（显示字符串）
	def __str__(self):
		return self._path
#直接显示的调用（内存地址）指向定制调用（设置的字符串）
	__repr__ = __str__

a = Chain()
print(a.status.user.timeline.list)