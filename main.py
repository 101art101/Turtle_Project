from turtle import *

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

