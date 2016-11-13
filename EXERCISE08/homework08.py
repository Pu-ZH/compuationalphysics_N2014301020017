import pylab as pl
import math

class bifurcation_diagram:
    def __init__(self,q=0.5,g=9.8,l=9.8,omegaD=2.0/3.0,FD=1.35,theta=0.200):
        self.q=q
        self.g=g
        self.l=l
        self.omegaD=omegaD
        self.FD=FD
        self.dt=2*math.pi/(500*omegaD)
        self.t=[0]
        self.w=[0]
        self.theta=[theta]
        self.fd=[]
        self.Theta=[]
        self.W=[]
     
    def run(self):     
        for i in range(10000):
            #计算摆的运动：
            self.w.append(self.w[-1]-(self.g/self.l)*math.sin(self.theta[-1])*self.dt-\
                    self.q*self.w[-1]*self.dt+self.FD*math.sin(self.omegaD*self.t[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            if self.theta[-1]>=math.pi:
                self.theta[-1]=self.theta[-1]-2*math.pi
            if self.theta[-1]<=-math.pi:
                self.theta[-1]=self.theta[-1]+2*math.pi
            self.t.append(self.t[-1]+self.dt)
        #根据self.w[i]的个数，每隔一个周期取出一组w、theta值进行作图：
        for i in range(len(self.w)/500-10):
            self.Theta.append(self.theta[500*(i+10)])
            self.W.append(self.w[500*(i+10)])
            self.fd.append(self.FD)

    def showresult(self):
        pl.plot(self.fd,self.Theta,'r.')
        pl.xlabel("FD(s)")
        pl.ylabel("$\\theta$(radians)")
        pl.show()

#将FD值按一定精度从1.35取至1.5：
i=1.35        
while i<1.489:
    a=bifurcation_diagram(FD=i)
    a.run()
    a.showresult()
    i=i+0.001