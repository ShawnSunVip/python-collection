# 功能描述
# by Shawn
# 开发时间: 2021/8/9 14:02

import turtle

def Peach_heart():
    turtle.color("red",'red')
    turtle.left(135)
    turtle.fd(100)
    turtle.right(180)
    turtle.circle(50,-180)
    turtle.left(90)
    turtle.circle(50,-180)
    turtle.right(180)
    turtle.fd(100)

Peach_heart()
turtle.penup()
turtle.goto(100,30)
turtle.pendown()
turtle.seth(0)
Peach_heart()

turtle.penup()
turtle.color("black")
turtle.goto(-100,30)
turtle.pendown()
turtle.seth(25)
turtle.fd(350)

turtle.done