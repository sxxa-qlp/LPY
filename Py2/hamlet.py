def getText():
	with open('hamlet.txt','r')as f:
		txt = str(f.read())
	txt = txt.lower()
	for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
		txt = txt.replace(ch,' ')
	return txt
hamletTxt = getText()
#切片操作，str---->list
words = hamletTxt.split()
counts = {}
for word in words:
	counts[word] = counts.get(word,0) + 1
#dict类型没有顺序---->有顺序的list
#返回的是元组数组---->([(),()])
# items = counts.items()
# print(items)
#返回list[(),()]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse = True)
for i in range(10):
	word , count = items[i]
	print('{0:<10},{1:>5}'.format(word,count))