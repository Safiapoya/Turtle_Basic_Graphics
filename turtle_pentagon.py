import turtle
wn = turtle.Screen()
wn.bgcolor("yellow")
pen = turtle.Turtle()

dis = 5
pen.speed(10)
pen.color = ("green")

for i in range(150):
    pen.forward(dis)
    pen.left(72)
    dis = dis+2
wn.exitonclick()
