EXERCISE13
=======
      
 - **作业要求**     
    习题6.9： 对一端固定另一端自由的弦的波动进行频谱分析。          
       
 - **作业代码链接**     
     [problem 6.9-1: Waves on a string(only one end fixed)](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-1.py)      
     [problem 6.9-2: String signal versus time](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-2.py)      
     [problem 6.9-3: Power spectrum](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-3.py)      

 - **作业内容**       
     波动运动的方程：     
     ![eq1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-eq1.png)     
     对弦上的一段微元段进行受力分析：        
     ![eq2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-eq2.png)             
     带入的到方程：     
     ![eq3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-eq3.png)      
     整理得到本次程序的算法：     
     ![eq4](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-eq4.png)            
     
     对于一端固定一段自由的弦，可以画出随时间变化的波动的图形。
     在t=0时刻在x=0.5L处有一个波包：     
     ![1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-1.png)        
     由此可以看出，与两端固定的波动相比，这种情况下波包在自由端返回时不会发生反向。        
     可以画出不同位置x上的定点的位置y随时间t变化的图像：     
     此为在中心点处：     
     ![2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-2.png)      
     改变x的位置进行对比：         
![15%](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-15.png)
![30%](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-30.png)
![45%](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-45.png)
![50%](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-50.png)
![75%](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-75.png)
![100%](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-100.png)          
     将边界条件稍作修改可以得到书上两端固定弦的图：
     ![2ends](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-2ENDS-5.png)        
     与书上一致。     
      
     通过快速傅里叶变换（FFT），可以得到各位置的功率谱：            
![5](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-F-P-5.png)
![15](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-F-P-15.png)
![30](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-F-P-30.png)
![45](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-F-P-45.png)
![50](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-F-P-50.png)
![75](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-F-P-75.png)
![100](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE13/homework13-F-P-100.png)      
 
     
