from turtle import *
from math import sqrt
global x0_triangle, y0_triangle
x0_triangle=0
y0_triangle=-200

t1 = Turtle()
main_win = t1.getscreen()
main_win.listen()


def paint_square_button(len_square):
    for i in range(4):
        t1.forward(len_square)
        t1.left(90)


def paint_triangle_button(len_triangle):
    for i in range(3):
        t1.forward(len_triangle)
        t1.left(120)


def paint_circle_button(len_circle):
    t1.circle(len_circle)
def move(x, y):
    t1.goto(x, y)
    global x1_triangle, y1_triangle , x0_triangle, y0_triangle
    print(x0_triangle, x1_triangle, y1_triangle, y0_triangle)
    if x < -100 and x > -200 and y > -200 and y < -100:
        len_square = int(input("Введите сторону квадрата"))
        t1.goto(0, 0)
        t1.pendown()
        paint_square_button(len_square)
        t1.penup()
    elif sqrt((x - 200) ** 2 + (y + 150) ** 2) <= 50:
        t1.goto(0, 0)
        len_circle = int(input("Введите радиус круга"))
        paint_circle_button(len_circle)
        t1.pendown()
        t1.circle(len_circle)
        t1.penup()
    elif (x0_triangle-x)*(y0_triangle-y0_triangle)-(x0_triangle+100-x0_triangle)*(y0_triangle-y)<0 and (x0_triangle+100-x)*(y1_triangle-y0_triangle)-(x1_triangle-x0_triangle+100)*(y0_triangle-y)<0 and (x1_triangle-x)*(y0_triangle-y1_triangle)-(x0_triangle-x1_triangle)*(y1_triangle-y)<0:
        len_triangle = int(input("Введите сторону треугольника"))
        t1.goto(0, 0)
        t1.pendown()
        paint_triangle_button(len_triangle)
        t1.penup()
    elif (x0_triangle-x)*(y0_triangle-y0_triangle)-(x0_triangle+100-x0_triangle)*(y0_triangle-y)>0 and (x0_triangle+100-x)*(y1_triangle-y0_triangle)-(x1_triangle-x0_triangle+100)*(y0_triangle-y)>0 and (x1_triangle-x)*(y0_triangle-y1_triangle)-(x0_triangle-x1_triangle)*(y1_triangle-y)>0:
        len_triangle = int(input("Введите сторону треугольника"))
        t1.goto(0, 0)
        t1.pendown()
        paint_triangle_button(len_triangle)
        t1.penup()
t1.penup()
t1.goto(-200, -200)
t1.pendown()
for i in range(4):
    t1.forward(100)
    t1.left(90)
t1.penup()
t1.goto(x0_triangle, y0_triangle)
t1.pendown()
for i in range(3):
    t1.forward(100)
    t1.left(120)
    if i==1:
        global x1_triangle, y1_triangle
        x1_triangle = t1.xcor()
        y1_triangle = t1.ycor()


    # x=t1.xcor()
# y=t1.ycor()
# print(x, y)
    # print(x, y)
t1.penup()
t1.goto(200, -200)
t1.pendown()
t1.circle(50)
t1.penup()
main_win.onscreenclick(move)
# if x<-100 and x>-200 and y>-200 and y<-100:
#     len_square=int(input("Введите сторону квадрата"))
#     paint_square_button(len_square)
# elif  sqrt((x - 200) ** 2 + (y +100) ** 2) <= 50:
#     len_circle=int(input("Введите радиус круга"))
#     paint_circle_button(len_circle)
#     t1.circle(len_circle)



x=t1.xcor()
y=t1.ycor()
print(x, y)




main_win.mainloop()

# 100 -200
# 50 -113
# -0 -200
# x = t1.xcor()
# y = t1.ycor()
# print(x, y)

# (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
# (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)
# (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)


# 1 x0_triangle=0 y0_triangle=-200
#     2 x0_triangle+100=100 y0_triangle=-200
#     3 x1_triangle= 50 y1_triangle=-113
#      (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
#       (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)
#       (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)
