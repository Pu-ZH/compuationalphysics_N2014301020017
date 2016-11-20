EXERCISE09
=======

 - **作业要求**  
    习题3.31：考虑体系弹性且光滑的情况下，弹球处于一个矩形边框以及一个矩形边框里的位于矩形中心（或偏离中心一点）的圆形（或椭圆）边框之间，与边界不断碰撞的运动的情况。          
    如书中P85 FIGURE3.21：小球在矩形边框内运动：      
    ![figure3.21](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE09/homework09-5.jpg)    
       
 - **作业代码链接**  
     [problem 3.31: The Billiard Problem](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE09/homework09.py)   
      
       
 - **作业内容**    
     本次作业的原理比较简单。   
     由于体系是弹性且光滑的，所以我们可以写出小球的运动方程：     
     ![1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE09/homework09-3.png)     
     而党校求遇到边界时，进行完全弹性碰撞，速度分量可写为：        
     ![1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE09/homework09-4.png)       
     故我认为本题的难点在于几何图形问题本身。      
     以下为我画出的运动轨迹，当圆形边界位于举行便捷的正中央：    
     ![2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE09/homework09-1.png)      
     当考虑圆形边界偏离举行中心的情况时，由于改写球型边界碰撞的过程较繁琐，故只需要改变矩形边框的位置便可简单地达到效果：         
     ![3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE09/homework09-2.png)      
     由此可见小球在矩形边界以及其中的球形边界之间的运动时杂乱无章的，且对于初始物理量十分敏感。
