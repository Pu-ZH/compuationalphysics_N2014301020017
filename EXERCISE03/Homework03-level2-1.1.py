   #1.1版本减少了电脑的运算量   
   #用line_N[X]语句，全部直接输出字符串的一部分  
   #省去了上一版本横向移动的循环中不断修改line_N的操作   

line_0 = "@PHYSICS@ "  
line_1 = "||    //  "
line_2 = "|| @ // @ "  
line_3 = " [###]  @ "  
line_4 = " |###|  @ "  
line_5 = " L###|  @ "  
line_6 = " || \\    "         #唯独显示不出连续的“\\"????不知是否为版本原因？？  
line_7 = " || //  @ "  
line_8 = " || @     "  
line_9 = " @        "  
   
xmax=70                       #改变xmax和ymax可改变横竖移动范围
ymax=30  
decelerationY=3                #改变decelerationY可调节y方向上移动的速度   
  
line_0 = xmax*" "+str(line_0)    #直接设定总line_N,以后直接输出其某部分
line_1 = xmax*" "+str(line_1)    #从左边延长字符串
line_2 = xmax*" "+str(line_2)  
line_3 = xmax*" "+str(line_3)  
line_4 = xmax*" "+str(line_4)  
line_5 = xmax*" "+str(line_5)  
line_6 = xmax*" "+str(line_6)  
line_7 = xmax*" "+str(line_7)  
line_8 = xmax*" "+str(line_8)  
line_9 = xmax*" "+str(line_9)
  
for x in range(xmax,-1,-1):    #右平移   
    import os  
    i = os.system('cls')       #省去了循环中不断修改line_N的操作
    print line_0[x:]  
    print line_1[x:]  
    print line_2[x:]  
    print line_3[x:]  
    print line_4[x:]  
    print line_5[x:]  
    print line_6[x:]  
    print line_7[x:]  
    print line_8[x:]  
    print line_9[x:]  
      
for y in range(ymax*decelerationY):       #下平移
    import os                             #不明提示???shadowed by loop variable
    i = os.system('cls')   
    y_deceleration = int(y/decelerationY)  
    for j in range(y_deceleration):  
        print " "  
    print line_0  
    print line_1  
    print line_2  
    print line_3  
    print line_4  
    print line_5  
    print line_6  
    print line_7  
    print line_8  
    print line_9
    
for m in range(xmax):                   #左平移
    import os  
    i = os.system('cls')  
    for j in range(y_deceleration):  
        print " "  
    print line_0[m:]                  #省去了循环中不断修改line_N的操作
    print line_1[m:]  
    print line_2[m:]  
    print line_3[m:]  
    print line_4[m:]  
    print line_5[m:]  
    print line_6[m:]  
    print line_7[m:]  
    print line_8[m:]  
    print line_9[m:]  
  
for y in range(ymax*decelerationY,0,-1):    #上平移
    import os  
    i = os.system('cls')  
    y_deceleration = int(y/decelerationY)  
    for j in range(y_deceleration):  
        print " "  
    print line_0[xmax:]  
    print line_1[xmax:]  
    print line_2[xmax:]  
    print line_3[xmax:]  
    print line_4[xmax:]  
    print line_5[xmax:]  
    print line_6[xmax:]  
    print line_7[xmax:]  
    print line_8[xmax:]  
    print line_9[xmax:]  
