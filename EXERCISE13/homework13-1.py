import pylab as pl
import math
import numpy as np

l=1.0
c=300.0
dx=0.01
dt=dx/c
r=c*dt/dx
ls=int(l/dx)
time=150
k=1000
y=[[0 for i in range(ls)]for n in range(time)]
yshow=[[0 for i in range(ls)]]
timestep=10

for i in range(ls):
    y[0][i]=math.exp(-k*(dx*i-0.5)**2)
    y[1][i]=math.exp(-k*(dx*i-0.5)**2)
    
for n in range(1,time-1):
    for i in range(1,ls-1):
        y[n+1][i]=2*(1-r**2)*y[n][i]-y[n-1][i]+r**2*(y[n][i+1]+y[n][i-1])
    y[n+1][ls-1]=(2-r**2)*y[n][ls-1]-y[n-1][ls-1]+r**2*y[n][ls-2]
    if n%timestep==1:
        yshow.append(y[n])

showplus1=np.array([1 for i in range(ls)])
showplus2=np.array([1.8 for i in range(ls)])
for a in range(len(yshow)):
    pl.plot(range(ls),yshow[a]/showplus2+showplus1*a)

pl.yticks(range(len(yshow)),(timestep*i for i in range(len(yshow))))
pl.ylabel("time(/y)")
pl.xlabel("x")
pl.show()



    


