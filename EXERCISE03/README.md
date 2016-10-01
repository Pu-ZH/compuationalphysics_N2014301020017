EXERCISE03
=======

 - **作业要求**  
   1. 在课程主页上复习这两次课程的内容，初步掌握python和matplotlib的语法规则，为接下来的课程做好准备   
   2. 作业L1 在屏幕上让你的英文名字水平移动起来  
   3. 作业L2 在80*80点阵上用字符拼出你想画的东西，并让它旋转起来，希望脑洞大开！（比如字符、火柴人、火箭等等）  
     
     
 - **作业链接**   
   [LEVEL 1：名字的平移](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/homework03level1.py)   
   [LEVEL 2：2.1_小人沿矩形走动](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/Homework03-level2-2.1.py)  
    - 其中2.1由[LEVEL 2:1.1_小人沿矩形四周平移](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/Homework03-level2-1.1.py)与[LEVEL 2:2.0_小人向前走路的动作](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/Homework03-level2-2.0.py)结合而成。  
   - [LEVEL2:审题错误？？用turtle画“旋转？”的星星](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/drawSTAR-2.0.py)

     
 - **作业截图**  
 LEVEL 1
------  
通过修改l和t的数值可调节字母横向移动的距离和时间：  
   ![homework03-level1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/homework03-level1.gif)    
  
LEVEL 2
------   
  - [homework03-level2_2.1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/Homework03-level2-2.1.py)  可让小人做出沿四周走动的动作，
      ![homework03-level2_2.1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/homework03-level2_2.1.gif)   
      由1.1(让小人沿四周平移、无动作，与[1.0](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/homework03-level2-1.0.py)相比简化了步骤，但效果相同)  和2.0(让小人向左平移时有脚步的动作，结束前“！”的图案有闪烁效果)结合起来, 做到小人沿四周走动的动作以及“！”的闪烁效果   
    用这种方法可以做出很多动作变换，但是受）目前自己语言知识的局限，方法十分笨拙！  
    1.1:![homework03-level2-1.1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/homework03-level2_1.1.gif)  
    2.0:![homework03-level2_2.0](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/homework03-level2_2.0.gif)  
  
  - [drawSTAR](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/drawSTAR-2.0.py) 是在“小人的走动”一系列程序之前写的。。。为了思考如何“旋转”，然而发现由于turtle虽然有不同的“笔”，但是只有一个“笔头”...即不能在同一时刻有多处笔头同时移动（或许有办法做到只是目前我知道的太少），导致星星的出现与消失必须交替进行，而且笔画的速度也较慢，因此做出来的效果与想象甚远。。。相比于[1.0](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/drawSTAR-1.0.py)的效果,[2.0](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/drawSTAR-2.0.py)保留了每颗星星出现的轨迹使其看起来更像在“旋转且变大”....然而严格的来讲，这并没能实现“旋转”，而“小人的走动”的方法却可以实现旋转，只不过要一张一张画很麻烦很笨拙罢了！  
     2.0:![drawSTAR_2.0](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/drawSTAR_2.0.gif)  
     1.0:![drawSTAR_1.0](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE03/drawSTAR_1.0.gif)



