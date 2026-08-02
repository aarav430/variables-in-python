import turtle

screen = turtle.Screen()
screen.title("Square using Turtle")
screen.bgcolor("lightblue")  

# Create turtle
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(3)

for i in range(4):
    pen.forward(100)
    pen.right(90)

pen.hideturtle()
turtle.done()