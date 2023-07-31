import turtle
wn = turtle.Screen()
wn.bgcolor("green")
ben = turtle.Turtle()

dis = 2
ben.speed(20)

for i in range(400):
    ben.forward(dis)
    ben.left(125)
    dis = dis+1