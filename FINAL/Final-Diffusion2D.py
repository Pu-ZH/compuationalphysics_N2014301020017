import pylab as pl
import random
import numpy as np

n=101           #n为步数，即时间
a=20.0        #容器为a乘a的
c=4.0
pnumber=4
m=pnumber**2   #一共有m个粒子分布在c乘c的初始位置


def run():
    xy=[[[i%pnumber*1.0/pnumber*c-c/2.0],[i/pnumber*1.0/pnumber*c-c/2.0]] for i in range(m)]
    
    pl.subplot(2,2,1)
    pl.title('Steps(=time)=0')
    pl.xlim(-a/2,a/2)
    pl.ylim(-a/2,a/2)
    pl.xlabel("x")
    pl.ylabel("y")
    for j in range(m):
        pl.plot(xy[j][0][-1],xy[j][1][-1],'.')


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
        if i==10:
            pl.subplot(2,2,2)
            pl.title('Steps(=time)=10')
            pl.xlim(-a/2,a/2)
            pl.ylim(-a/2,a/2)
            pl.xlabel("x")
            pl.ylabel("y")
            for j in range(m):
                pl.plot(xy[j][0][-1],xy[j][1][-1],'.')
        if i==50:
            pl.subplot(2,2,3)
            pl.title('Steps(=time)=50')
            pl.xlim(-a/2,a/2)
            pl.ylim(-a/2,a/2)
            pl.xlabel("x")
            pl.ylabel("y")
            for j in range(m):
                pl.plot(xy[j][0][-1],xy[j][1][-1],'.')
        if i==100:
            pl.subplot(2,2,4)
            pl.title('Steps(=time)=100')
            pl.xlim(-a/2,a/2)
            pl.ylim(-a/2,a/2)
            pl.xlabel("x")
            pl.ylabel("y")
            for j in range(m):
                pl.plot(xy[j][0][-1],xy[j][1][-1],'.')


run()
pl.show()




