import turtle   
wn = turtle.Screen()   
wn.bgcolor("darkblue")                  #设置背景颜色  
  
ace = turtle.Turtle()                   #画笔“ace”
ace.shape("blank")  
ace.pensize(6)   
ace.penup()    
   
eraser = turtle.Turtle()                #橡皮擦“eraser”
eraser.color("darkblue")  
eraser.shape("blank")  
eraser.pensize(3)  
eraser.penup()  
  
def drawSTAR(t,sz,distance):             #定义函数 drawSTAR 
    t.goto(0,0)                           #使其每次画完回到原点   
    t.left(15+2*distance)                 #改变每个星星起笔位置：使其旋转且扩散 
    t.forward(3*distance)  
    t.pendown()  
    for star in range(5):  
        t.forward(sz)  
        t.right(36)  
        t.forward(sz)  
        t.left(108)  
    t.penup()  
      
list = ["silver","yellow","hotpink","lightblue","lightgreen","BlueViolet"]  
for j in range(3,18,3):  
    d = j/3  
    c = list[d%6]                                 #除以颜色数的余数
    ace.color(c)  
    drawSTAR(ace,j,d)  
                      #分两个循环，让画完几个星星之后再从第一个开始擦掉     
for j in range(18,90,3):  
    d = j/3  
    c = list[d%5]  
    ace.color(c)  
    drawSTAR(ace,j,d)  
    drawSTAR(eraser,j-15,d-5)  
  
wn.exitonclick()           
