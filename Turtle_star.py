#star
import turtle
wn= turtle.Screen()
wn.bgcolor("lightblue")
star= turtle.Turtle()
star.pensize(10)
star.color("white")

Star= turtle.Turtle()
Star.pensize(5)
Star.color("Yellow")

dis = 200

for i in range(5):
    star.forward(dis)
    star.left(145)

for i in range(5):
    Star.forward(dis)
    Star.left(145)