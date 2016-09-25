   #2.01版本  
   #试图让小人走起来。可用同样的方式套用到1.1中  
   #可调节x方向速度；增加感叹号的闪烁效果  
   #but extremely ugly！   
  
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
  
xmax=100                       #改变xmax和ymax可改变横竖移动范围
decelerationX=3                #为改变x方向速度，增加decelerationX
shiningtimes = 5               #可改变感叹号闪烁次数
  
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
    import os                             
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
        

