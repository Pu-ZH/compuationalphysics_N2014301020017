import pylab as pl
import math

class KeplersThirdLaw:
    def __init__(self,MS=2.0*10**30,GMS=4*math.pi**2,\
                 beta=2.0,\
                 MP=5.7*10**26,a=9.54,e=0.056):          
        #此处MP、a、e三个量根据所求星球的参数修改
        
        self.MS=MS        
        self.GMS=GMS
        self.MP=MP
        self.a=a
        self.e=e
        self.x=[a*(1+e)]
        self.y=[0]
        self.r=[a*(1+e)]
        self.vx=[0]
        self.vy=[(GMS*(1-e)*(1+MP/MS)/(a*(1+e)))**0.5]
        self.beta=beta
        self.F=[GMS*MP/(a**beta)]
        self.dt=0.002
        self.t=[0]
        self.v=[(GMS*(1-e)*(1+MP/MS)/(a*(1+e)))**0.5]
        self.xshow=[a*(1+e)+e*a]
        
    def run(self):
        while(1):
            self.r.append((self.x[-1]**2+self.y[-1]**2)**0.5)
            self.F.append(self.GMS*self.MP/(self.r[-1]**self.beta))
            self.vx.append(self.vx[-1]-(self.F[-1]/self.MP)*self.x[-1]/self.r[-1]*self.dt)
            self.vy.append(self.vy[-1]-(self.F[-1]/self.MP)*self.y[-1]/self.r[-1]*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            self.v.append((self.vx[-1]**2+self.vy[-1]**2)**0.5)
            self.xshow.append(self.x[-1]+self.e*self.a)
            if(self.y[-2]<0 and self.y[-1]>=0):
                break
            #当self.y从小于0变为大于等于0的时候结束循环
            
    def showresult(self):
        pl.title("Kepler's Third Law")
        
        pl.plot(self.xshow,self.y,'m-')
        pl.text(self.x[30],self.y[30],'Saturn',color='magenta',size=20)
        pl.plot(self.e*self.a,0,'mx')

        pl.plot(0,0,'rp')
        pl.text(-0.2,0.1,'SUN',color='red',size=20)
        
        pl.xlim(-0.2-max(self.xshow),0.2+max(self.xshow))
        pl.ylim(-0.2-max(self.xshow),0.2+max(self.xshow))
        pl.xlabel("X(AU)")
        pl.ylabel("Y(AU)")
        pl.show()
        
        print "星球质量MP：",self.MP,";a=",self.a,";e=",self.e
        print "x轴最大距离：",min(self.x),max(self.x)
        print "y轴最大距离：",min(self.y),max(self.y)
        print "最大速度：",max(self.v),";最小速度：",min(self.v)
        print "模拟得到的周期T=",self.t[-1]
        print "T^2/a^3=",(self.t[-2])**2/self.a**3
        
a=KeplersThirdLaw()
a.run()
a.showresult()
