EXERCISE10  
=======

 - **作业要求**  
    习题4.8：，运行模拟行星的运动，计算出T2/a3，以证明椭圆轨道下的开普勒第三定律。      
     这里有太阳系的一些行星以及它们的椭圆轨道的c数据：    
    ![1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-planet1.jpg)     
       
 - **作业代码链接**      
      [problem 4.8: 开普勒第三定律](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10.py)   
      
       
 - **作业内容**    
     （注：本次作业的时间、长度单位分别为：yr，AU）
     太阳系中的行星的轨道方程满足：    
     ![eq2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-eq2.png)     
     并可以得到速度最大最小值：     
     ![eq3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-eq3.png)     
     由euler cromer calculate公式:可以得到算法：    
     ![eq1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-eq1.png)    
     
     
     把几个行星的参数带入程序，进行模拟，得到以下曲线（图中原点（0,0）为太阳位置；"X"为各轨道的椭圆中心）：      
     ![SOLAR](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-solar.png)       
     并且计算出了各行星的T3/a2值：    
     Venus(金)：    
     ![V](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-venus.png)    
     Earth(地)：     
     ![E](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-earth.png)    
     Mars(火)：      
     ![M](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-mars.png)    
     Jupiter(木)：    
     ![V](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-jupiter.png)    
     Saturn(土)：     
     ![V](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-saturn.png)     
     
     将其值与书中资料对比：      
     ![t3/a2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-planet2.jpg)        
     有一定的误差，不过大体上非常相近，且均趋近于1.0，因此可以证明开普勒第三定律：        
     绕以太阳为焦点的椭圆轨道运行的所有行星，其各自椭圆轨道半长轴的立方与周期的平方之比是一个常量。          
     
      
     另：将程序简单修改后可探究beta=2.0时轨道的稳定性。以下为行星在几种beta值下运行若干周期的轨迹：    
![beta1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-2_2.png)
![beta2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-2.05_2.png)
![beta3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-2.05_10.png)
![beta4](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-2.5_2.png)
![beta5](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE10/homework10-3.0_1.png)        
     以此可以观察到beta不为2.0时行星难以回到初始状态，只有beta=2.0时轨道是最稳定的。  
