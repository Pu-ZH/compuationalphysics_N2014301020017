import pylab as pl
import random
import numpy as np

n=700  
m=5            
r2ave=np.array([0 for i in range(n)])
step_number=range(n)

#pl.subplot(1,2,1)
for j in range(m):
    xy=[[0],[0]]
    r2=[0]
    for i in range(1,n):
        k=random.choice([0,1])
        xy[k].append(xy[k][-1]+random.choice([-1,1]))   
        xy[k-1].append(xy[abs(k)-1][-1])       
        r2.append(xy[k][-1]**2+xy[k-1][-1]**2)
        r2ave[i]=r2ave[i]+r2[-1]
        pl.plot(xy[0],xy[1],'.')

pl.xlim(-50,50)
pl.ylim(-50,50)
pl.xlabel("x")
pl.ylabel("y")
pl.title('random walk in 2 dimension')
pl.show()