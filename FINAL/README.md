FINAL PROJECT: RANDOM SYSTEM
=======
      
 - **目的：**       
    基于书上Chapter 7：Random System，对于一维与高维度随机系统中的''Random Walk''(即“醉汉走路”)的运动进行模拟，并探究相关物理问题。      
       
 - **代码链接：**      
     [Final: Random walk in 1 dimension](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/Final-RWI1D-1.py)         
     [Final: Random walk in 3 dimensions](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/Final-RWI3D.py)        
     [Final: Diffusion in 2 dimensions](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/Final-Diffusion2D.py)       
    
 - **模拟与探究：**       
     ![picture 1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/picture1.jpg)      
     所谓“Random walk”（醉汉走路）的模型即为：      
     质点小球（“醉汉”）在一维空间内行走（从原点0开始），每次步长相等（记为1），但是行走的方向是随机的，向左与向右的概率均为1/2。我们将重点讨论其均方位移（“MSD”，即mean squared displacement）对时间t（也等同于步数step number）之间的关系。         
       
     1、最基础的情况（一维）：       
     首先由题，其经过n步之后的位置满足：              
     ![eq1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/eq1.png)                 
     以统计学的角度出发，当走足够多的步数时、测量的次数足够多时，其均方位移的期望值为：       
     ![eq2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/eq2.png)          
     均方位移的大小是与步数n（也就是时间t）成正比的。    
     其意义在于：当我们模拟的组数增多时，这几组的均方位移对步数n的变化曲线应该是越来越趋近于上面这条直线的。我们对这种情况进行模拟[(Final: Random walk in 1 dimension)](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/Final-RWI1D-1.py)，分别作出x和均方位移对时间的曲线（步数均为1500）：     
     模拟组数为3：     
     ![1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/1.png)      
      模拟组数为30：    
     ![2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/2.png)    
      模拟组数为100：    
     ![3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/3.png)     
     模拟组数为500：    
     ![4](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/4.png)     
     显然，模拟的结果证实了我们的推断。    
     这也满足方程：![eq3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/eq3.png)    
     其中D为扩散系数，d为维数（此时为1），t为时间也就是步数n。        
     故：在1维等步长的情况下：D=1/2。        
      
    2、一维变形1——方向有一定程度的选择：       
    若向左与向右的概率不为0.5，则x对t的曲线应根据向左向右概率的大小而向上或向下偏移不同的程度。        
    ![eq3.5](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/eq3.5.png)：         
     ![5](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/5.png)![6](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/6.png)        
     实验结果符合预期。     
     
    3、一维变形2——步长不等，从（-1,1）中随机：    
     在足够多的试验次数之下：    
     ![eq4](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/eq4.png)     
     则得到这种情况下D=1/6。     
     模拟的时候，只需修改小小的随机代码[(Final: Random walk in 1 dimension-2)](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/Final-RWI1D-2.py)就可得到结果（实验组数:左图5，右图100）：      
     ![7](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/7.png)![8](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/8.png)     
     实验结果符合预期。     
     
    4、高维变形——探究高维度的均方位移对步数n（时间t）的曲线：     
    通过与一维类似的分析方法相结合可知，在高维情况下，等步长与随机步长时的D值均不变(为了方便表示，此处不变的D记为刚才公式中乘了d(维度)之后的D，否则高维度的D还要除以维度数d)：     
    ![eq5](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/eq5.png)     
    对三维[(Final: Random walk in 3 dimensions)](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/Final-RWI3D.py) 与二维[(Final: Random walk in 2 dimensions)](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/Final-RWI2D.py) 情况（等步长与随机步长，实验组数为200）进行模拟来验证上述分析：
    ![9](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/9.png)![10](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/10.png)      
    满足预期，故分析得到验证。      
     
    5、二维变形——模拟扩散：      
    为了更直观地观察随机系统，对二维状态下的一块初始为矩形分布的粒子群在一个容器中的扩散进行了模拟[Final: Diffusion in 2 dimensions](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/Final-Diffusion2D.py)。      
    可以修改粒子数、粒子初始分布的范围以及容器的边界大小：      
    ![11](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/11.png)![12](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/12.png)![13](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/FINAL/13.png)     
    在此程序基础上，我们可以对扩散现象进行更深入的模拟与研究，但目前遇到了一些困难，故本次探究就暂时告一段落，以后有机会将继续探究！       
       
 - **致谢：**       
 致谢蔡浩老师一学期的授课！    
 还有平时一起探讨计算物理问题的同学们！     
 还有致谢教材的辅导：    
 《Computational Physics》——Nicholas J. Giordano , Hisao Nakanishi    
 《Think Python: How to Think Like a Computer Scientist》——Allen B. Downey    
