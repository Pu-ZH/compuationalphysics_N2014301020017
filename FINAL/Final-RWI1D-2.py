import pylab as pl
import random
import numpy as np

n=3000                          #n为每次模拟的步数
m=50                             #m为醉汉的个数，即模拟次数
x2ave=np.array([0 for i in range(n)])
step_number=range(n)

pl.subplot(1,2,1)
for j in range(m):
    x=[0]
    x2=[0]
    for i in range(1,n):
        x.append(x[-1]+random.uniform(-1,1)) 
        x2.append(x[-1]**2)
        x2ave[i]=x2ave[i]+x2[-1]

    pl.plot(step_number,x,'.')
    pl.xlabel("step number")
    pl.ylabel("x")
    pl.title('random walk in one dimension')
pl.plot(step_number,[0 for i in range(n)],'c--',lw=5)

pl.subplot(1,2,2)
pl.plot(step_number,x2ave/m,'m.')
pl.plot([i for i in range(n)],[1.0/3.0*i for i in range(n)],'c--',lw=5)
pl.xlabel("step number(=time)")
pl.ylabel("<x$^2$>")
pl.title('<x$^2$>versus time')
pl.show()