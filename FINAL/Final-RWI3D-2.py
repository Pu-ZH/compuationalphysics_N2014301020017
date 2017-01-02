import pylab as pl
import random
import numpy as np

n=1000                           #n为每次模拟的步数
m=100                             #m为醉汉的个数，即模拟次数
r2ave=np.array([0 for i in range(n)])
step_number=range(n)

for j in range(m):
    xyz=[[0],[0],[0]]
    r2=[0]
    for i in range(1,n):
        
        k=random.choice([0,1,-1])          #随机从xyz中选择一个方向
        xyz[k].append(xyz[k][-1]+random.uniform(-1,1))   
        xyz[abs(k)-1].append(xyz[abs(k)-1][-1])
        xyz[1-k-abs(k)].append(xyz[1-k-abs(k)][-1])        
#这里用k选择移动的方向，用[abs(k)-1]与[1-k-abs(k)]选择另外两个没移动的方向
        r2.append(xyz[k][-1]**2+xyz[abs(k)-1][-1]**2+xyz[1-k-abs(k)][-1]**2)
        r2ave[i]=r2ave[i]+r2[-1]

pl.plot(step_number,r2ave/m,'m.')
pl.plot([i for i in range(n)],[1.0/3.0*i for i in range(n)],'c--',lw=5)
pl.xlabel("step number(=time)")
pl.ylabel("<r$^2$>")
pl.title('<r$^2$>versus time(random walk in 3 dimension)')
pl.show()
