from turtle import *


def draw_christree():

    speed(10) # Painting speed control
    bgcolor("Dark red") #choose the background color
    pensize(10) #Define the pensize
    penup()
    goto(0, -250) #Move the pen to the target pixel
    fillcolor("#000000")
    begin_fill()
    pendown()
    seth(110)
    fd(445)
    seth(250)
    fd(445)
    seth(0)
    fd(345)
    seth(60)
    fd(350)
    seth(150)
    fd(16)
    seth(240)
    fd(360)
    penup()
    end_fill()
    
    fillcolor("#000000")
    goto(-50,120)
    pendown()
    begin_fill()
    circle(-120)
    end_fill()
    circle(-120,180)
    seth(100)
    fd(60)
    seth(315)
    fd(55)
    penup()
    
    
    goto(-50,120)
    pendown()
    seth(-120)
    circle(-120)
    circle(-120,180+120)
    seth(80)
    fd(60)
    seth(225)
    fd(55)
    
    penup()




    goto(300, -250) #Move the pen to the target pixel
    fillcolor("#ffffff")
    begin_fill()
    pendown()
    seth(110)
    fd(245)
    seth(250)
    fd(245)
    seth(0)
    fd(185)
    seth(60)
    fd(150)
    seth(150)
    fd(8)
    seth(240)
    fd(160)
    penup()
    end_fill()
    
    fillcolor("#ffffff")
    goto(270,0)
    pendown()
    begin_fill()
    circle(-60)
    end_fill()
    circle(-60,180)
    seth(100)
    fd(40)
    seth(315)
    fd(35)
    penup()
    
    goto(270,0)
    pendown()
    seth(-120)
    circle(-60)
    circle(-60,180+120)
    seth(80)
    fd(40)
    seth(225)
    fd(35)
    
    
    
    penup()
    fd(1000000)


draw_christree()
