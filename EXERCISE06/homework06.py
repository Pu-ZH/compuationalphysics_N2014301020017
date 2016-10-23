import pylab as pl
import math

print"开始计算"

class cannon_shell_toward_target:
    def __init__(self,g=9.8,time_step=0.01,b2=0.004,m=1,T0=288.15,alpha=2.5,a=0.0065,\
    x_target=12000,y_target=1200,x0=0,y0=0,v0=500,theta=math.pi/4,):
        self.g=g
        self.dt=time_step
        self.B2=[b2]
        self.m=m
        self.T0=T0
        self.alpha=alpha
        self.a=a
        self.x_target=x_target
        self.y_target=y_target
        self.x=[x0]
        self.y=[y0]
        self.v=[v0]
        self.vx=[v0*math.cos(theta)]
        self.vy=[v0*math.sin(theta)]
        self.d=[(self.x_target**2+self.y_target**2)**0.5]
        self.vq=[0]
        self.thetaq=[0]

        
    def run(self):
        while(self.x[-1]<self.x_target or self.y[-1]>self.y_target):
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)           
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.B2.append(self.B2[0]*(1-self.a*self.y[-1]/self.T0)**self.alpha)
            self.vx.append(self.vx[-1]-self.B2[-1]*self.v[-1]*self.vx[-1]/self.m*self.dt)
            self.vy.append(self.vy[-1]-self.g*self.dt-self.B2[-1]*self.v[-1]*self.vy[-1]/self.m*self.dt)
            self.v.append((self.vx[-1]**2+self.vy[-1]**2)**0.5)
            if(((self.x[-1]-self.x_target)**2+(self.y[-1]-self.y_target)**2)**0.5<self.d[-1]):
                self.d.append(((self.x[-1]-self.x_target)**2+(self.y[-1]-self.y_target)**2)**0.5)
                self.vq.append(self.v[0])
                self.thetaq.append(self.theta[0])

            
            
    def show_results(self):
        font = {'family': 'serif', 
                'color':  'darkblue', 
                'weight': 'normal', 
                'size': 16, 
        } 
        pl.plot(self.x_target,self.y_target,"r*")
        pl.plot(self.x,self.y)
        pl.title('Trajectory of cannon shell',fontdict = font)
        pl.xlabel('x')
        pl.ylabel('y')
        pl.show()

    def choose(self):                            #改变角度、改变速度，找出最小值
        for i in range(2000,500,1):
            dmin2=(self.x_target**2+self.y_target**2)**0.5
            for j in range(90,0,1):
                dmin1=(self.x_target**2+self.y_target**2)**0.5
                a=cannon_shell_toward_target(v0=i,theta=j*math.pi/180)
                a.run()
                if(self.d[-1]<dmin1):
                    dmin1=self.a
                    v_min1=self.vq[-1]
                    theta_min1=self.thetaq[-1]
            if(dmin1<dmin2):
                dmin2=dmin1
                v_min2=v_min1
                theta_min2=theta_min1
        a=cannon_shell_toward_target(v0=v_min2,theta=theta_min2)
        a.run()
        a.showresults()
        print "发射角度为",theta_min2
        print "发射初速度",v_min2
        print "距目标最短距离",dmin2

a=cannon_shell_toward_target()
a.choose()
print"结束计算"