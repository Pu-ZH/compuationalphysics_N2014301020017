import pylab as pl
import math

print"开始计算"

class cannon_shell_toward_target:
    def __init__(self,g=9.8,time_step=0.01,b2=0.00004,m=1,T0=288.15,alpha=2.5,a=0.0065,\
    x_target=30000,y_target=1000,x0=0,y0=0,v0=500,theta=math.pi/4,):
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
        self.theta=[theta]
        self.vx=[v0*math.cos(theta)]
        self.vy=[v0*math.sin(theta)]


        
    def run(self):
        global d,vq,thetaq                                  #定义全球变量，否则该变量到了choose程序里显示没有定义
        d=(self.x_target**2+self.y_target**2)**0.5
        vq=0
        thetaq=0
        while(self.y[-1]>=self.y[0] or self.y[-1]>=self.y_target):
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)           
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.B2.append(self.B2[0]*(1-self.a*self.y[-1]/self.T0)**self.alpha)
            self.vx.append(self.vx[-1]-self.B2[-1]*self.v[-1]*self.vx[-1]/self.m*self.dt)
            self.vy.append(self.vy[-1]-self.g*self.dt-self.B2[-1]*self.v[-1]*self.vy[-1]/self.m*self.dt)
            self.v.append((self.vx[-1]**2+self.vy[-1]**2)**0.5)
            d_self=((self.x[-1]-self.x_target)**2+(self.y[-1]-self.y_target)**2)**0.5
            if(d_self<d):                                             #为了寻找出该轨迹离目标点的最小距离
                d=d_self
                vq=self.v[0]
                thetaq=self.theta[0]
        print ".",          #打印"."是为了让人知道程序是否在正常运行，还是进入了死循环。后面输出dmin的值同理

    def draw(self):
        while(self.x[-1]<self.x_target or self.y[-1]>self.y_target):
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)           
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.B2.append(self.B2[0]*(1-self.a*self.y[-1]/self.T0)**self.alpha)
            self.vx.append(self.vx[-1]-self.B2[-1]*self.v[-1]*self.vx[-1]/self.m*self.dt)
            self.vy.append(self.vy[-1]-self.g*self.dt-self.B2[-1]*self.v[-1]*self.vy[-1]/self.m*self.dt)
            self.v.append((self.vx[-1]**2+self.vy[-1]**2)**0.5)
            
            
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
        pl.xlim(0,32000)
        pl.ylim(0,10000)
        pl.show()

     #需注意：速度、角度取值过大时，y值过大，可能导致系数(1-self.a*self.y[-1]/self.T0)<0从而报错
    def choose(self):                            #改变角度、改变速度，找出最小值
        dmin2=(self.x_target**2+self.y_target**2)**0.5 
        dmin1=(self.x_target**2+self.y_target**2)**0.5
        for i in range(300,1500,100):    
            j=0
            while(j<60):
                a=cannon_shell_toward_target(v0=i,theta=j*math.pi/180)
                a.run()
                if(d<dmin1):
                    dmin1=d
                    v_min1=vq
                    theta_min1=thetaq
                    print "dmin1=",dmin1
                j=j+5
            if(dmin1<dmin2):
                dmin2=dmin1
                v_min2=v_min1
                theta_min2=theta_min1
            print "dmin2=",dmin2
        a=cannon_shell_toward_target(v0=v_min2,theta=theta_min2)
        a.draw()
        a.show_results()
        print "得到结论："
        print "发射角度为",theta_min2*180/math.pi,"°"
        print "发射初速度",v_min2
        print "距目标最短距离",dmin2


a=cannon_shell_toward_target()
a.choose()
print"结束计算"