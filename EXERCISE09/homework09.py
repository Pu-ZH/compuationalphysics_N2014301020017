# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:19:56 2016

@author: phb-pc
"""

import pylab as pl
import math

class billiard_problem:
    def __init__(self,x0=-0.99,y0=-0.99,xl=-1,xr=1.5,yd=-1,yu=1.5,R=0.5,\
                   v0=0.1,theta0=math.pi/7,timestep=0.03):
        self.x=[x0]
        self.y=[y0]
        self.xl=xl
        self.xr=xr
        self.yd=yd
        self.yu=yu
        self.r=R
        self.vx=[v0*math.cos(theta0)]
        self.vy=[v0*math.sin(theta0)]
        self.v0=v0
        self.theta=[theta0]
        self.t=[0]
        self.dt=timestep
        self.cx=[R]
        self.cy=[0]
        
    def run(self):
        i=0
        while(i<=20000):
            if not (self.xl<=self.x[-1]<=self.xr):
                self.theta.append(math.pi-self.theta[-1])
            if not (self.yd<=self.y[-1]<=self.yu):
                self.theta.append(-self.theta[-1])                           
            if (self.x[-1]**2+self.y[-1]**2<self.r**2):
                self.theta.append(2*math.atan(self.vy[-1]/self.vx[-1])+math.atan(self.y[-1]/self.x[-1]))              
            #遇到边界反向
      
            self.vx.append(self.v0*math.cos(self.theta[-1]))
            self.vy.append(self.v0*math.sin(self.theta[-1]))
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            i=i+1
            
    def drawcircle(self):
        i=0
        while (i<2*math.pi):
            self.cx.append(self.r*math.cos(i))
            self.cy.append(self.r*math.sin(i))
            i=i+0.1
    
    
    
    def showresult(self):
        pl.plot(self.x,self.y,'r.')
        pl.plot(self.cx,self.cy,'b*')
        pl.xlim(self.xl,self.xr)
        pl.ylim(self.yd,self.yu)
        pl.xlabel("x")
        pl.ylabel("y")
        pl.show()
        
a=billiard_problem()
a.run()
a.drawcircle()
a.showresult()