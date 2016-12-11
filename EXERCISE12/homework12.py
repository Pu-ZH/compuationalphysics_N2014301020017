import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-1,1,0.05)
y=np.arange(-1,1,0.05)
V=[[0. for i in xrange(len(x))]]
dV=1
mindV=0.0001*len(x)                  #最后V的改变量小于此精度时便停止update

for i in xrange(1,len(x)):
    tmp = [0.]
    for j in range(1,len(y)):
        if len(x)/3<=i<=len(x)*2/3 and len(y)/3<=j<=len(y)*2/3:
            tmp.append(1.0)
        else:
            tmp.append(0.0)                #初始化V,除了中间V=1其余区域V=0
    V.append(tmp)


while dV>mindV:
    dV=0
    for i in xrange(1,len(x)-1):
        for j in xrange(1,len(y)-1):
            if len(x)/3<=i<=len(x)*2/3 and len(y)/3<=j<=len(y)*2/3 or\
            i==1 or j==1:
                continue
            tmp=(V[i-1][j]+V[i+1][j]+V[i][j-1]+V[i][j+1])/4
            dV=dV+np.abs(tmp-V[i][j])
            V[i][j]=tmp


x,y=np.meshgrid(x,y)
ax=plt.subplot(111,projection='3d')
surf = ax.plot_surface(x,y,V,rstride=2,cstride=2,cmap=plt.cm.coolwarm,alpha=0.8)
ax.set_title("Electric Potential")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V')
ax.set_zlim(-0.20, 1.20)