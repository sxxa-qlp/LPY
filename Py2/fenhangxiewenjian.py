fo = open('name.txt','w+')
ls = ['1001','XIAOMING','1701ban']
for i in ls:
	fo.writelines(i+'\n')
#注意移动文件读取指针到指定位置（文件开始）
fo.seek(0)
for line in fo:
	print(line)
fo.close()