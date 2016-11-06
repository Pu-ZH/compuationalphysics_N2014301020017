EXERCISE07
=======

 - **作业要求**  
    习题3.13：
       
       
 - **作业链接：**[problem 2.10: 精确打击不同高度的目标](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE06/homework06.py)    
      
       
 - **作业内容（上次提交作业时我的Spyder出了点问题，导致程序无法正常运行。现已重新上传了改正后的程序。）**    
    本次作业要考虑海拔高度与迎面风阻的影响，算法要进行以下改进：  
     考虑风阻![1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE06/QQ%E5%9B%BE%E7%89%8720161027001314.png)  
     则![4](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE06/QQ%E5%9B%BE%E7%89%8720161027001345.png)   
     考虑海拔影响![2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE06/QQ%E5%9B%BE%E7%89%8720161027001437.png)  
     故只需每个B2乘ρ0后面的那个一个关于y的系数![3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE06/QQ%E5%9B%BE%E7%89%8720161027001420.png)即可。  
    
      
    关于找到打击目标的发射速度、发射角度：
    为了精确打击到高度与发射点不同的目标，我用了两个循环分别对炮弹的发射速度与发射角度进行扫描，逐个比较不同炮弹轨迹距目标点的最小距离，从而最后筛选出一个距目标最近的炮弹轨迹，并画出它的轨迹曲线，从而达到精确打击目标。   
    但是由于越精确的扫描要求大量的运行时间，所以我先以范围广、精度低的方式扫描一遍，得到了所求炮弹发射速度、角度的粗略值，再在该粗略估计值附近进行较精确的扫描，从而在一定程度上缩短运行时间、提高打击精确度。
    如图，对坐标为（30000，1000）的目标，先进行粗略扫描：速度300~1500每隔100扫描一次，角度0~60°每隔5°扫描一次。得到粗略值：
 ![homework06-1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE06/homework06-1.png)  
   
   再在小范围内进行精确的扫描：  
 ![homework06-2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE06/homework06-2.png)   
    从而得到了打击目标的炮弹发射速度、发射角度。   
    由于程序运行时间过长，可以在循环中适当即时输出一些符号或者变量的值，可以帮助你知道程序运行的进程。  
