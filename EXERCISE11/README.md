EXERCISE11
=======

 - **作业要求**  
    习题4.19、4.20：     
               模拟画出Hyperion模型，对于微小的theta角度差，两个系统的theta角的差值随时间t变化的曲线。         
               如果去掉theta在-π~+π之间的这个限制条件的情况下曲线会是怎么样？           
       
 - **作业代码链接**       
     [problem 4.19、4.20: Chaotic Tumbling of Hyperion](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11.py)   
      
       
 - **作业内容**      
     ![1](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/416fe6f77a9c07804980adf458799d95.gif)       
         三体问题（three-body problem）是天体力学中的基本力学模型。它是指三个质量、初始位置和初始速度都是任意的可视为质点的天体，在相互之间万有引力的作用下的运动规律问题。      
         以目前已知的知识和方法并不能精确求解所有的三体问题，只能研究及种特定的情况。       
     ![2](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/f42455bf301fb0dfab6e6bb9ce00cdf6.gif)
     ![3](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/9e98db8cf47db0c6ef50ff02703dec12.gif)     
     三体问题最简单的一个例子就是太阳系中太阳、地球和月球的运动。          
     在宇宙中可以把星球看成质点，如果不计太阳系其他星球的影响，那么它们的运动就只是在引力的作用下产生的，所以我们就可以把它们的运动看成一个三体问题。    
     ![4](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/22f55a9fb506989e9fbe3e199d4cfe02.gif)     
         
        土卫七是太阳系中最大的一颗高度不规则（非球形）天体，绕着Saturn(土星)运动。       
        1848年美国天文学家邦德（G. Bond）和英国的拉塞尔（W. Lassell）各自独立发现土卫七，距土星1482000公里，像大星体的碎片，表面有如海绵，是目前所发现太阳系中最大的一颗非球形天体，也是太阳系中已知星体中唯一一个自转会混沌的星体，每21.3天绕土星旋转一周。     
         我们在这里研究Hyperion(土卫七)的运动：      
     ![figure4.16](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/figure4.16.jpg)     
         可以得到运动方程对其theta角进行模拟：          
     ![eq](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/e1.png)        
      
        通过修改theta初始值可以得到theta(0)=0.0与theta(0)=0.01的两条轨道的theta差值随之间t变化的曲线。（模拟中长度单位：HU,时间单位：Hyperion-year）     
        通过修改质心得初始速度而改变圆形轨道还是椭圆轨道（肌酸得初始速度为2π时为圆形轨道）。     
        以下为模拟所的曲线。     
        单个系统在圆形轨道上运动的theta与w随t变化曲线：         
     ![5](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11-theta-c.png)
     ![6](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11-w-c.png)      
         单个系统在椭圆轨道（我们取初始速度为5）上运动的theta与w随t变化曲线：          
     ![7](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11-theta-e.png)
     ![8](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11-w-e.png)       
         两个系统（初始theta差为0.01）的theta差随t变化曲线：               
         圆轨道：    
     ![9](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11-dtheta-c.png)      
         椭圆轨道：    
     ![10](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11-dtheta-e.png)        
         由此可见模型在轨道中的运动对初始theta值十分敏感。     
     
     另：     
         再去掉限制条件“theta在-π~+π之间”：      
         圆轨道：    
     ![11](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11-dtheta-c-2.png)      
         椭圆轨道：    
     ![12](https://github.com/Pu-ZH/compuationalphysics_N2014301020017/blob/master/EXERCISE11/homework11-dtheta-e-2.png)     
         我们发现去掉限制条件之后两个曲线的一些跳变值不见了。     
 
