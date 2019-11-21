L = ['ASLDJF','ASDFdkfd']
def normalize(name):
	return name[0].upper() + name[1:].lower()
b = list(map(normalize,L))
print(b)