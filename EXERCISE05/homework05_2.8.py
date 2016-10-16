import pylab as pl
import math

r0=6371000
G=6.67*10**-11              #引力常数
M=5.977*10**24              #地球质量
g0=G*M/r0**2                #地面上的初始重力加速度

class Cannon_shell_trajectories:
    def __init__(self,x0=0,y0=0, time_step=0.1,\
                 total_time=17, initial_velocity=100, initial_angle=math.pi/3):
        self.r = [r0]        
        self.g = [g0]
        self.x = [x0]
        self.y = [y0]
        self.v = [initial_velocity]
        self.t = [0]
        self.dt = time_step
        self.time = total_time
        self.vx=[initial_velocity*math.cos(initial_angle)]
        self.vy=[initial_velocity*math.sin(initial_angle)]
    def run(self):
        _time = 0
        _x=0
        _y=0
        _r=r0
        _g=g0
        while(_time < self.time):
            self.vy.append(self.vy[-1] - self.dt * self.g[-1])
            self.x.append(_x)
            _x += self.vx[-1]*self.dt
            self.y.append(_y)
            _y += self.vy[-1]*self.dt
            self.r.append(_r)
            _r = self.r[-1]+self.y[-1]
            self.g.append(_g)
            _g=G*M/self.r[-1]**2
            self.t.append(_time)
            _time += self.dt 
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }

        pl.plot(self.x, self.y)
        pl.title('Cannon shell trajectories ', fontdict = font)
        pl.xlabel('x ')
        pl.ylabel('y ')
        pl.text(0.2 * self.time, 0.9 * self.v[-1],\
                'ignoring both air drag and the effect of air density', fontdict = font)
        pl.show()

a = Cannon_shell_trajectories()
a.run()
a.show_results()