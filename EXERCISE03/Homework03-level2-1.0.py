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
decelerationY=2                #y方向的减速系数  
  
for x in range(xmax):          #右平移  
    line_0 = " "+str(line_0)   #从左边延长字符串
    line_1 = " "+str(line_1)  
    line_2 = " "+str(line_2)  
    line_3 = " "+str(line_3)  
    line_4 = " "+str(line_4)  
    line_5 = " "+str(line_5)  
    line_6 = " "+str(line_6)  
    line_7 = " "+str(line_7)  
    line_8 = " "+str(line_8)  
    line_9 = " "+str(line_9)  
    import os  
    i = os.system('cls')  
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
      
for y in range(ymax*decelerationY):  #下平移  
    import os                       #不明提示???shadowed by loop variable
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
    
for m in range(xmax):                      #左平移  
    import os  
    i = os.system('cls')  
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
    line_0 = line_0[1:]               #截取字符串
    line_1 = line_1[1:]  
    line_2 = line_2[1:]  
    line_3 = line_3[1:]  
    line_4 = line_4[1:]  
    line_5 = line_5[1:]  
    line_6 = line_6[1:]  
    line_7 = line_7[1:]  
    line_8 = line_8[1:]  
    line_9 = line_9[1:]  
  
for y in range(ymax*decelerationY,0,-1):   #上平移   
    import os  
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
  
