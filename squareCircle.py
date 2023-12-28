import turtle
turtle.bgcolor('black')

square = turtle.Turtle()
square.speed(10)
square.pencolor('red')
for i in range(200):
    square.forward(i)
    square.left(91)