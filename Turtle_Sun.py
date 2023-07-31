#sun

import turtle
wn = turtle.Screen()
sun = turtle.Turtle()

dis = 4
sun.speed(20)

for i in range(430):
    sun.forward(dis)
    sun.left(190)
    dis = dis+2
