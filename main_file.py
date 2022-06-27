from turtle import Turtle, Screen
from paddle import Paddle
import time
from user_paddle import UserPaddle

#paddle
# paddle1 = Paddle()
# paddle1.create_paddle(6, "white")
# paddle1.center_paddle(-350)
#
# user_paddle = UserPaddle()


# screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

user_paddle = UserPaddle()

# setup
screen.tracer(n=0, delay=0)
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


# listening
screen.listen()
screen.onkeypress(user_paddle.down, "Down")
screen.onkeypress(user_paddle.up, "Up")
screen.tracer(True)
is_on = True
#gameloop
while is_on == True:
    screen.update()



screen.exitonclick()
