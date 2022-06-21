from turtle import Turtle, Screen
from user_paddle import Paddle

#paddle
user_paddle = Paddle()

# screen setup
screen = Screen()
screen.tracer(n=0, delay=0)
screen.bgcolor("black")
screen_setup_turtle = Turtle()
screen_setup_turtle.color("white")
screen_setup_turtle.penup()
screen_setup_turtle.goto(0, 400)
screen_setup_turtle.setheading(270)
screen_setup_turtle.pensize(5)
for x in range(27):
    screen_setup_turtle.pendown()
    screen_setup_turtle.forward(10)
    screen_setup_turtle.penup()
    screen_setup_turtle.forward(20)
#screen setup



screen.exitonclick()
