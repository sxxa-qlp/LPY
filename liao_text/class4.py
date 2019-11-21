class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')
class  Cat(Animal):
	def run(self):
		print('Cat is running...')
def run_twice(Animal):
	Animal.run()
	Animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

run_twice(Animal())
run_twice(Cat())
class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')
#拷贝忍者——卡卡西，无血缘关系复制手印即可施术
class Timer(object):
	def run(self):
		print('Start')
run_twice(Timer())
