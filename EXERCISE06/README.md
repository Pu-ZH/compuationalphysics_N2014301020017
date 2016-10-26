EXERCISE06(已更新)
=======

 - **作业要求**  
    习题2.10（升级版）：使炮弹打到一个高度与发射点不同处的目标。   
    作业L1 2.10题强化版（引入迎面风阻）  
    作业L2 2.10题进一步升级，发展“超级辅助精确打击系统”（考虑炮弹初始发射的时候发射角度误差度，速度有5%的误差，迎面风阻误差10%，以炮弹落点与打击目标距离差平方均值最小为优胜） 
   
    以上所有计算需要考虑海拔高度的影响，使用绝热模型进行计算，误差描述使用最简单的均匀分布描述（也就是在误差范围内每个取值概率是一样的）。  
    完成L2作业的同学，下次上课可以比赛，对100km的目标看谁打得最精确！   
       
       
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

