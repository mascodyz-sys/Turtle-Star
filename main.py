
import turtle
# Create screen
screen = turtle.Screen()
screen.setup(width=400, height=300)
screen.bgcolor("white")
screen.title("Turtle Start Example")
# Create turtle
t = turtle.Turtle()
t.pencolor("blue")
t.pensize(2)
# Draw a square
for _ in range(4):
   t.forward(100)
   t.right(90)
screen.exitonclick()
