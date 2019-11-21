import jieba
f = open('out1.txt','w')
fi = open("data.txt","r",encoding="utf-8")

d={}
for i in fi.readlines():
    for s in '，“”。、：（）':
        i=i.replace(s,'')
        i=i.strip()
    for w in jieba.lcut(i):
        d[w]=d.get(w,0)+1

ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)

for word in ls:
    if word[1]>=3:
        f.write(word[0]+'\n')

    
fi.close()
f.close()
