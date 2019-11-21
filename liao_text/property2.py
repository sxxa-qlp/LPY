class Screen(object):
	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height

	@width.setter
	def width(self,value):
		if isinstance(value,int):
			self._width = value
		else:
			raise TypeError('enter int')
	
	@height.setter
	def height(self,value):

		self._height = value 


	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =  ',s.resolution)



