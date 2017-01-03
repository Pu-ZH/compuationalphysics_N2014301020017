import pylab as pl
import random
import numpy as np
import math

n=100000           #n为步数，即时间
a=8.0        #容器为a乘a的
c=4.0
pnumber=4
m=pnumber**2   #一共有m个粒子分布在c乘c的初始位置

N=10

for p in range(N):
    xy=[[[i%pnumber*1.0/pnumber*c-c/2.0],[i/pnumber*1.0/pnumber*c-c/2.0]] for i in range(m)]
    P=[[[0 for l in range(n)] for j in range(int(a))] for i in range(int(a))]   #P[i][j][t]为第i行j列的格子里t时有粒子的概率

    for i in range(1,n):
        for j in range(m):        
            k=random.choice([0,1])        #随机选择运动方向
            plus=random.uniform(-1,1)     #随机选择运动距离
            if not -a/2<=xy[j][k][-1]+plus<a/2:
                j=j-1            
                continue   #另j=j-1，重新本次循环
            else:
                xy[j][k].append(xy[j][k][-1]+plus)  
                xy[j][k-1].append(xy[j][k-1][-1])    
        P[int(xy[j][k][-1])][int(xy[j][k-1][-1])][i]=+1.0/N

S=[0 for l in range(n)]
for l in range(n):
    for i in range(int(a)):
        for j in range(int(a)):
            S[l]=S[l]-P[i][j][l]*math.log(P[i][j][l]+0.000001)     #???
        
pl.plot(range(n),S)
pl.show()




