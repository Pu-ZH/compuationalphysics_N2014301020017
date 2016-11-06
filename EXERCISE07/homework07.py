import pylab as pl
import math

class two_nearly_identifical_pendulums:
    def __init__(self,q=0.5,g=9.8,l=9.8,omegaD=2.0/3.0,FD=0.5,time_step=0.04,\
                 theta1=0.201,theta2=0.200,total_time=50):
        self.q=q
        self.g=g
        self.l=l
        self.omegaD=omegaD
        self.FD=FD
        self.dt=time_step
        self.t=[0]
        self.total_time=total_time
        self.w1=[0]
        self.w2=[0]
        self.theta1=[theta1]
        self.theta2=[theta2]
        self.Dtheta=[theta1-theta2]
        self.line=[0]                                     #为画线用
        
    def run(self):
        i=0        
        while self.t[-1]<=self.total_time:
            #摆1的计算：
            self.w1.append(self.w1[-1]-(self.g/self.l)*math.sin(self.theta1[-1])*self.dt-\
                    self.q*self.w1[-1]*self.dt+self.FD*math.sin(self.omegaD*self.t[-1])*self.dt)
            self.theta1.append(self.theta1[-1]+self.w1[-1]*self.dt)
            if self.theta1[-1]>=math.pi:
                self.theta1[-1]=self.theta1[-1]-2*math.pi
            if self.theta1[-1]<=-math.pi:
                self.theta1[-1]=self.theta1[-1]+2*math.pi
            
            #摆2的计算：
            self.w2.append(self.w2[-1]-(self.g/self.l)*math.sin(self.theta2[-1])*self.dt-\
                    self.q*self.w2[-1]*self.dt+self.FD*math.sin(self.omegaD*self.t[-1])*self.dt)
            self.theta2.append(self.theta2[-1]+self.w2[-1]*self.dt)
            if self.theta2[-1]>=math.pi:
                self.theta2[-1]=self.theta2[-1]-2*math.pi
            if self.theta2[-1]<=-math.pi:
                self.theta2[-1]=self.theta2[-1]+2*math.pi
                
            #计算Δtheta、完成循环：
            self.Dtheta.append(math.log(abs(self.theta1[-1]-self.theta2[-1])))
            self.t.append(self.t[-1]+self.dt)
            i+=1
            
        #计算斜率（只是粗略估计的，并不精确）并画出虚线：
        k=(self.Dtheta[-1]-self.Dtheta[1])/self.t[-1]
        i=0
        while self.t[i]<=self.total_time:
            self.line.append(self.Dtheta[1]+k*i*self.dt)
            i+=1
        print "FD=",self.FD
        print "斜率k=",k
    
    def showresult(self):
        pl.plot(self.t,self.Dtheta)
        pl.plot(self.t,self.line,'--')
        pl.xlabel("time(s)")
        pl.ylabel("Δtheta(radians)")
        pl.show()
                
a=two_nearly_identifical_pendulums()
a.run()
a.showresult()