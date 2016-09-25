# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 18:11:00 2016

@author: puzhenhang
"""


   #2.1版本  
   #将2.1套入1.1中，让小人走一整圈  

  
Aline_0 = "@PHYSICS@ "          #向右走  
Aline_1 = "||    //  "  
Aline_2 = "|| @ // @ "  
Aline_3 = " [###]  @ "  
Aline_4 = " |###|  @ "  
Aline_5 = " L###|  @ "  
Aline_6 = " ||  \    "         #唯独显示不出连续的“\\"????不知是否为版本原因？？  
Aline_7 = " ||   \ @ "  
Aline_8 = " ||    @  "  
Aline_9 = " @        "  
  
Bline_0 = "@PHYSICS@ "  
Bline_1 = "||    //  "  
Bline_2 = "|| @ // @ "  
Bline_3 = " [###]  @ "  
Bline_4 = " |###|  @ "  
Bline_5 = " L###|  @ "  
Bline_6 = "  \ ||    "  
Bline_7 = "   \||  @ "  
Bline_8 = "    @     "  
Bline_9 = "    @     "  
  
Cline_0 = "@PHYSICS@ "  
Cline_1 = "||    //  "  
Cline_2 = "|| @ // @ "  
Cline_3 = " [###]  @ "  
Cline_4 = " |###|  @ "  
Cline_5 = " L###|  @ "  
Cline_6 = " || ||    "         #唯独显示不出连续的“\\"????不知是否为版本原因？？  
Cline_7 = " || ||  @ "  
Cline_8 = " || ||    "  
Cline_9 = "  @  @    "  
  
Dline_0 = " @PHYSICS@"         #向左走  
Dline_1 = "  \\    ||"  
Dline_2 = "   \\ @ ||"  
Dline_3 = "    [###] "  
Dline_4 = "    |###| "  
Dline_5 = "    |###] "  
Dline_6 = "    /  || "  
Dline_7 = "   /   || "  
Dline_8 = "  @    || "  
Dline_9 = "        @ "  
  
Eline_0 = " @PHYSICS@"  
Eline_1 = "  \\    ||"  
Eline_2 = "   \\ @ ||"  
Eline_3 = "    [###] "  
Eline_4 = "    |###| "  
Eline_5 = "    |###] "  
Eline_6 = "    || /  "  
Eline_7 = "    ||/   "  
Eline_8 = "     @    "  
Eline_9 = "     @    "  
  
Fline_0 = " @PHYSICS@"  
Fline_1 = "  \\    ||"  
Fline_2 = "   \\ @ ||"  
Fline_3 = "    [###] "  
Fline_4 = "    |###| "  
Fline_5 = "    |###] "  
Fline_6 = "    || || "  
Fline_7 = "    || || "  
Fline_8 = "    || || "  
Fline_9 = "    @  @ "  
   
xmax=70                       #改变xmax和ymax可改变横竖移动范围  
ymax=30  
shiningtimes = 5               #可改变感叹号每回闪烁次数  
decelerationY = 3  
decelerationX = 3                #为改变x方向速度，增加decelerationX  

  
Aline_0 = xmax*" "+str(Aline_0)    #A  
Aline_1 = xmax*" "+str(Aline_1)    
Aline_2 = xmax*" "+str(Aline_2)  
Aline_3 = xmax*" "+str(Aline_3)  
Aline_4 = xmax*" "+str(Aline_4)  
Aline_5 = xmax*" "+str(Aline_5)  
Aline_6 = xmax*" "+str(Aline_6)  
Aline_7 = xmax*" "+str(Aline_7)  
Aline_8 = xmax*" "+str(Aline_8)  
Aline_9 = xmax*" "+str(Aline_9)  

Bline_0 = xmax*" "+str(Bline_0)    #B  
Bline_1 = xmax*" "+str(Bline_1)    
Bline_2 = xmax*" "+str(Bline_2)  
Bline_3 = xmax*" "+str(Bline_3)  
Bline_4 = xmax*" "+str(Bline_4)  
Bline_5 = xmax*" "+str(Bline_5)  
Bline_6 = xmax*" "+str(Bline_6)  
Bline_7 = xmax*" "+str(Bline_7)  
Bline_8 = xmax*" "+str(Bline_8)  
Bline_9 = xmax*" "+str(Bline_9)  

Cline_0 = xmax*" "+str(Cline_0)    #C  
Cline_1 = xmax*" "+str(Cline_1)   
Cline_2 = xmax*" "+str(Cline_2)  
Cline_3 = xmax*" "+str(Cline_3)  
Cline_4 = xmax*" "+str(Cline_4)  
Cline_5 = xmax*" "+str(Cline_5)  
Cline_6 = xmax*" "+str(Cline_6)  
Cline_7 = xmax*" "+str(Cline_7)  
Cline_8 = xmax*" "+str(Cline_8)  
Cline_9 = xmax*" "+str(Cline_9)  
  
Eline_0 = xmax*" "+str(Eline_0)    #E  
Eline_1 = xmax*" "+str(Eline_1)    
Eline_2 = xmax*" "+str(Eline_2)  
Eline_3 = xmax*" "+str(Eline_3)  
Eline_4 = xmax*" "+str(Eline_4)  
Eline_5 = xmax*" "+str(Eline_5)  
Eline_6 = xmax*" "+str(Eline_6)  
Eline_7 = xmax*" "+str(Eline_7)  
Eline_8 = xmax*" "+str(Eline_8)  
Eline_9 = xmax*" "+str(Eline_9)  
  
Fline_0 = xmax*" "+str(Fline_0)    #F  
Fline_1 = xmax*" "+str(Fline_1)    
Fline_2 = xmax*" "+str(Fline_2)  
Fline_3 = xmax*" "+str(Fline_3)  
Fline_4 = xmax*" "+str(Fline_4)  
Fline_5 = xmax*" "+str(Fline_5)  
Fline_6 = xmax*" "+str(Fline_6)  
Fline_7 = xmax*" "+str(Fline_7)  
Fline_8 = xmax*" "+str(Fline_8)  
Fline_9 = xmax*" "+str(Fline_9)  
  
Dline_0 = xmax*" "+str(Dline_0)    #D  
Dline_1 = xmax*" "+str(Dline_1)   
Dline_2 = xmax*" "+str(Dline_2)  
Dline_3 = xmax*" "+str(Dline_3)  
Dline_4 = xmax*" "+str(Dline_4)  
Dline_5 = xmax*" "+str(Dline_5)  
Dline_6 = xmax*" "+str(Dline_6)  
Dline_7 = xmax*" "+str(Dline_7)  
Dline_8 = xmax*" "+str(Dline_8)  
Dline_9 = xmax*" "+str(Dline_9)  
  
for x in range(xmax*decelerationX,-1,-1):    #右平移   
    import os  
    i = os.system('cls')       #省去了循环中不断修改line_N的操作
    x_deceleration = int(x/decelerationX) 
    if x%26<=2 or 13<=x%20<=15:
        print Cline_0[x_deceleration:]  
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:]  
        print Cline_3[x_deceleration:]  
        print Cline_4[x_deceleration:]  
        print Cline_5[x_deceleration:]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:]  
    elif 15<=x%26<=25:
        print Aline_0[x_deceleration:]  
        print Aline_1[x_deceleration:]  
        print Aline_2[x_deceleration:]  
        print Aline_3[x_deceleration:]  
        print Aline_4[x_deceleration:]  
        print Aline_5[x_deceleration:]  
        print Aline_6[x_deceleration:]  
        print Aline_7[x_deceleration:]  
        print Aline_8[x_deceleration:]  
        print Aline_9[x_deceleration:]  
    elif 3<=x%26<=12:
        print Bline_0[x_deceleration:]  
        print Bline_1[x_deceleration:]  
        print Bline_2[x_deceleration:]  
        print Bline_3[x_deceleration:]  
        print Bline_4[x_deceleration:]  
        print Bline_5[x_deceleration:]  
        print Bline_6[x_deceleration:]  
        print Bline_7[x_deceleration:]  
        print Bline_8[x_deceleration:]   
        print Bline_9[x_deceleration:]   
        
for s in range(shiningtimes*20):         #增加：感叹号的闪烁效果  
    import os                            #不明提示???shadowed by loop variable  
    i = os.system('cls')   
    if s%20<=9:  
        print Cline_0[x_deceleration:]  
        print Cline_1[x_deceleration:]  
        print Cline_2[:-2]  
        print Cline_3[:-2]  
        print Cline_4[:-2]  
        print Cline_5[:-2]  
        print Cline_6[x_deceleration:]  
        print Cline_7[:-2]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:] 
    else:  
        print Cline_0[x_deceleration:]    
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:]  
        print Cline_3[x_deceleration:]  
        print Cline_4[x_deceleration:]  
        print Cline_5[x_deceleration:]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:]  
        
for y in range(ymax*decelerationY):       #下平移
    import os      
    i = os.system('cls')   
    y_deceleration = int(y/decelerationY)  
    for j in range(y_deceleration):  
        print " "  
    if y%26<=2 or 13<=y%20<=15:
        print Cline_0[x_deceleration:]  
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:]  
        print Cline_3[x_deceleration:]  
        print Cline_4[x_deceleration:]  
        print Cline_5[x_deceleration:]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:]  
    elif 15<=y%26<=25:
        print Aline_0[x_deceleration:]  
        print Aline_1[x_deceleration:]  
        print Aline_2[x_deceleration:]  
        print Aline_3[x_deceleration:]  
        print Aline_4[x_deceleration:]  
        print Aline_5[x_deceleration:]  
        print Aline_6[x_deceleration:]  
        print Aline_7[x_deceleration:]  
        print Aline_8[x_deceleration:]  
        print Aline_9[x_deceleration:]  
    elif 3<=y%26<=12:
        print Bline_0[x_deceleration:]  
        print Bline_1[x_deceleration:]  
        print Bline_2[x_deceleration:]  
        print Bline_3[x_deceleration:]  
        print Bline_4[x_deceleration:]  
        print Bline_5[x_deceleration:]  
        print Bline_6[x_deceleration:]  
        print Bline_7[x_deceleration:]  
        print Bline_8[x_deceleration:]   
        print Bline_9[x_deceleration:]   
        
for s in range(shiningtimes*20):         #2*感叹号的闪烁效果  
    import os                             
    i = os.system('cls')   
    for j in range(ymax):  
        print " "      
    if s%20<=9:  
        print Cline_0[x_deceleration:]  
        print Cline_1[x_deceleration:]  
        print Cline_2[:-2]  
        print Cline_3[:-2]  
        print Cline_4[:-2]  
        print Cline_5[:-2]  
        print Cline_6[x_deceleration:]  
        print Cline_7[:-2]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:] 
    else:  
        print Cline_0[x_deceleration:]    
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:]  
        print Cline_3[x_deceleration:]  
        print Cline_4[x_deceleration:]  
        print Cline_5[x_deceleration:]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:]  
    
for x in range(xmax*decelerationX):         #左平移
    import os  
    i = os.system('cls')   
    x_deceleration = int(x/decelerationX) 
    for j in range(ymax):  
        print " "  
    if x%26<=2 or 13<=x%20<=15:
        print Fline_0[x_deceleration:]  
        print Fline_1[x_deceleration:]  
        print Fline_2[x_deceleration:]  
        print Fline_3[x_deceleration:]  
        print Fline_4[x_deceleration:]  
        print Fline_5[x_deceleration:]  
        print Fline_6[x_deceleration:]  
        print Fline_7[x_deceleration:]  
        print Fline_8[x_deceleration:]  
        print Fline_9[x_deceleration:]  
    elif 15<=x%26<=25:
        print Eline_0[x_deceleration:]  
        print Eline_1[x_deceleration:]  
        print Eline_2[x_deceleration:]  
        print Eline_3[x_deceleration:]  
        print Eline_4[x_deceleration:]  
        print Eline_5[x_deceleration:]  
        print Eline_6[x_deceleration:]  
        print Eline_7[x_deceleration:]  
        print Eline_8[x_deceleration:]  
        print Eline_9[x_deceleration:]  
    elif 3<=x%26<=12:
        print Dline_0[x_deceleration:]  
        print Dline_1[x_deceleration:]  
        print Dline_2[x_deceleration:]  
        print Dline_3[x_deceleration:]  
        print Dline_4[x_deceleration:]  
        print Dline_5[x_deceleration:]  
        print Dline_6[x_deceleration:]  
        print Dline_7[x_deceleration:]  
        print Dline_8[x_deceleration:]   
        print Dline_9[x_deceleration:]   
        
for s in range(shiningtimes*20):         #3*感叹号的闪烁效果  
    import os                             
    i = os.system('cls')   
    for j in range(ymax):  
        print " "      
    if s%20<=9:  
        print Cline_0[x_deceleration:]  
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:-2]  
        print Cline_3[x_deceleration:-2]  
        print Cline_4[x_deceleration:-2]  
        print Cline_5[x_deceleration:-2]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:-2]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:] 
    else:  
        print Cline_0[x_deceleration:]    
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:]  
        print Cline_3[x_deceleration:]  
        print Cline_4[x_deceleration:]  
        print Cline_5[x_deceleration:]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:]  
        
for y in range(ymax*decelerationY,0,-1):     #上平移  
    import os      
    i = os.system('cls')   
    y_deceleration = int(y/decelerationY)  
    for j in range(y_deceleration):  
        print " "  
    if y%26<=2 or 13<=y%20<=15:
        print Cline_0[x_deceleration:]  
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:]  
        print Cline_3[x_deceleration:]  
        print Cline_4[x_deceleration:]  
        print Cline_5[x_deceleration:]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:]  
    elif 15<=y%26<=25:
        print Aline_0[x_deceleration:]  
        print Aline_1[x_deceleration:]  
        print Aline_2[x_deceleration:]  
        print Aline_3[x_deceleration:]  
        print Aline_4[x_deceleration:]  
        print Aline_5[x_deceleration:]  
        print Aline_6[x_deceleration:]  
        print Aline_7[x_deceleration:]  
        print Aline_8[x_deceleration:]  
        print Aline_9[x_deceleration:]  
    elif 3<=y%26<=12:
        print Bline_0[x_deceleration:]  
        print Bline_1[x_deceleration:]  
        print Bline_2[x_deceleration:]  
        print Bline_3[x_deceleration:]  
        print Bline_4[x_deceleration:]  
        print Bline_5[x_deceleration:]  
        print Bline_6[x_deceleration:]  
        print Bline_7[x_deceleration:]  
        print Bline_8[x_deceleration:]   
        print Bline_9[x_deceleration:]   
  
for s in range(shiningtimes*20):         #4*感叹号的闪烁效果  
    import os                             
    i = os.system('cls')   
    if s%20<=9:  
        print Cline_0[x_deceleration:]  
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:-2]  
        print Cline_3[x_deceleration:-2]  
        print Cline_4[x_deceleration:-2]  
        print Cline_5[x_deceleration:-2]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:-2]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:] 
    else:  
        print Cline_0[x_deceleration:]    
        print Cline_1[x_deceleration:]  
        print Cline_2[x_deceleration:]  
        print Cline_3[x_deceleration:]  
        print Cline_4[x_deceleration:]  
        print Cline_5[x_deceleration:]  
        print Cline_6[x_deceleration:]  
        print Cline_7[x_deceleration:]  
        print Cline_8[x_deceleration:]  
        print Cline_9[x_deceleration:]  
