EXERCISE07
=======

 - **作业要求**  
    习题3.13：计算两个几乎完全相同的摆，在如图Figure3.7的相应的lyapunov指数下的角度差的对数值（即log（Δθ））与时间（t）的关系。    
    ![figure3.7](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07-9.jpg)    
       
 - **作业代码链接**[problem 3.13: 两个相似的摆的（log（Δθ））与（t）的关系](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07.py)   
      
       
 - **作业内容**    
     由euler cromer calculate公式:    
     ![1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07-8.png)    
     可以得到算法：   
     ![2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07-7.png)    
     
     编写程序，可以通过在程序中修改FD的值：     
     ![3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07-5.png)    
     
     以得到以下曲线：    
     ![4](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07-1.png)    
     ![5](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07-2.png)   
     
     图中的斜率k，也就是此公式中的λ（等式两边取对数）：    
     ![6](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07-10.png)    
     
     不过这里的斜率k只是粗略估计值，并不准确。    
     
     ps：在编写程序的过程中发现书上的一处错误：    
     ![7](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE07/homework07-6.jpg)  
     公式中的“+”、“-”符号存在错误，否则画不出来正确的图像。     
     
     鸣谢!余剑桥 探讨程序、检查错误。
