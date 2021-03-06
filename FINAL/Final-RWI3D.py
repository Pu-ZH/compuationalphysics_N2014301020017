import pylab as pl
import random
import numpy as np

n=1000       
m=100 
r2ave=np.array([0 for i in range(n)])
step_number=range(n)

pl.subplot(1,2,1)
for j in range(m):
    xyz=[[0],[0],[0]]
    r2=[0]
    for i in range(1,n):
        k=random.choice([0,1,-1]) 
        xyz[k].append(xyz[k][-1]+random.choice([-1,1]))   
        xyz[abs(k)-1].append(xyz[abs(k)-1][-1])
        xyz[1-k-abs(k)].append(xyz[1-k-abs(k)][-1])        
        r2.append(xyz[k][-1]**2+xyz[abs(k)-1][-1]**2+xyz[1-k-abs(k)][-1]**2)
        r2ave[i]=r2ave[i]+r2[-1]

pl.plot(step_number,r2ave/m,'m.')
pl.plot([i for i in range(n)],[i for i in range(n)],'c--',lw=5)
pl.xlabel("step number(=time)")
pl.ylabel("<r$^2$>")
pl.title('fixed step lenth(3D)')

pl.subplot(1,2,2)
r2ave=np.array([0 for i in range(n)])
for j in range(m):
    xyz=[[0],[0],[0]]
    r2=[0]
    for i in range(1,n):
        k=random.choice([0,1,-1])
        xyz[k].append(xyz[k][-1]+random.uniform(-1,1))   
        xyz[abs(k)-1].append(xyz[abs(k)-1][-1])
        xyz[1-k-abs(k)].append(xyz[1-k-abs(k)][-1])        
        r2.append(xyz[k][-1]**2+xyz[abs(k)-1][-1]**2+xyz[1-k-abs(k)][-1]**2)
        r2ave[i]=r2ave[i]+r2[-1]
pl.plot(step_number,r2ave/m,'m.')
pl.plot([i for i in range(n)],[1.0/3.0*i for i in range(n)],'c--',lw=5)
pl.xlabel("step number(=time)")
pl.ylabel("<r$^2$>")
pl.title('random step length(3D)')
pl.show()