#注意方程组的描述以及print输出位置
a = 0
for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            if i>j>k and i+ j + k <100:
                if 1/pow(k,2) == 1/pow(i,2)+1/pow(j,2):
                    a += 1 
                    print(i,j,k)
print('共有{:}组解'.format(a))                    
                     

                