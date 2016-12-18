import pylab as pl
import math
import numpy as np

l=1.0
c=300.0
dx=0.01
dt=dx/c
r=c*dt/dx
ls=int(l/dx)
time=2000
k=1000
y=[[0 for i in range(ls)]for n in range(time)]
t=[0]
yshow=[0]

for i in range(ls):
    y[0][i]=math.exp(-k*(dx*i-0.5)**2)
    y[1][i]=math.exp(-k*(dx*i-0.5)**2)
    
for n in range(1,time-1):
    for i in range(1,ls-1):
        y[n+1][i]=2*(1-r**2)*y[n][i]-y[n-1][i]+r**2*(y[n][i+1]+y[n][i-1])
    y[n+1][ls-1]=(2-r**2)*y[n][ls-1]-y[n-1][ls-1]+r**2*y[n][ls-2]
    t.append(t[-1]+dt)
    yshow.append(y[n][int(ls*0.3)])

yshowplus=abs(np.fft.rfft(yshow))**2
f=np.linspace(0,int(1/dt/2),len(yshowplus))


pl.plot(f,yshowplus)
pl.xlim(0,5000)
pl.xlabel("frequency (Hz)")
pl.ylabel("power (arbitrary units)")
pl.text(1750,0.9*max(yshowplus),'30% from the fixed end',size='15')
pl.show()