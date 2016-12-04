import pylab as pl
import math

class ChaoticTumblingOfHyperion:
    def __init__(self,GMsat=4*math.pi**2.0,dt=0.0001,
                 theta1=0,theta2=0.01,v0=5.0,r0=1.0):
        self.GMsat=GMsat
        self.x=[r0]
        self.y=[0]
        self.r=[r0]
        self.vx=[0]
        self.vy=[v0]
        self.w1=[0]
        self.theta1=[theta1]
        self.w2=[0]
        self.theta2=[theta2]
        self.dt=dt
        self.t=[0]
        self.Fm=[GMsat/r0**2]
        self.dtheta=[abs(theta1-theta2)]
        
    def run(self):
        while (self.t[-1]<=6):
            self.r.append((self.x[-1]**2+self.y[-1]**2)**0.5)
            self.Fm.append(self.GMsat/self.r[-1]**2.0)
            self.vx.append(self.vx[-1]-self.Fm[-1]*self.x[-1]/self.r[-1]*self.dt)
            self.vy.append(self.vy[-1]-self.Fm[-1]*self.y[-1]/self.r[-1]*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.w1.append(self.w1[-1]-3*self.GMsat/self.r[-1]**5*(self.x[-1]*\
                          math.sin(self.theta1[-1])-self.y[-1]*math.cos(self.theta1[-1]))*\
                          (self.x[-1]*math.cos(self.theta1[-1])+self.y[-1]*\
                          math.sin(self.theta1[-1]))*self.dt)
            self.theta1.append(self.theta1[-1]+self.w1[-1]*self.dt)
            if not(-math.pi<self.theta1[-1]<math.pi):
                if(self.theta1[-1]>=math.pi):
                    self.theta1[-1]=self.theta1[-1]-2*math.pi
                if(self.theta1[-1]<=-math.pi):
                    self.theta1[-1]=self.theta1[-1]+2*math.pi
                    
            self.w2.append(self.w2[-1]-3*self.GMsat/self.r[-1]**5*(self.x[-1]*\
                          math.sin(self.theta2[-1])-self.y[-1]*math.cos(self.theta2[-1]))*\
                          (self.x[-1]*math.cos(self.theta2[-1])+self.y[-1]*\
                          math.sin(self.theta2[-1]))*self.dt)
            self.theta2.append(self.theta2[-1]+self.w2[-1]*self.dt)
            if not(-math.pi<self.theta2[-1]<math.pi):
                if(self.theta2[-1]>=math.pi):
                    self.theta2[-1]=self.theta2[-1]-2*math.pi
                if(self.theta2[-1]<=-math.pi):
                    self.theta2[-1]=self.theta2[-1]+2*math.pi
            self.dtheta.append(abs(self.theta1[-1]-self.theta2[-1]))
            self.t.append(self.t[-1]+self.dt)
            
    def showresult(self):
        pl.title('Hyperion dtheta versus time')
        pl.semilogy(self.t,self.dtheta)
        pl.xlim(0,8)
        pl.xlabel("time(Hyperion-year)")
        pl.ylabel("$\\delta$$\\theta$(radians)")
        pl.show()


a=ChaoticTumblingOfHyperion()
a.run()
a.showresult()
        
        
