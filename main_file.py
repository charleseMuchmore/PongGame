from turtle import Turtle, Screen
from paddle import Paddle

#paddle
paddle = Paddle()
paddle.create_paddle(5, "white")
paddle.center_paddle(-350)
for item in paddle.paddle_pieces:
    print(f"{item.pos()}")

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
