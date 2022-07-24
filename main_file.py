from turtle import Screen
from paddle import Paddle
from screen_setup import ScreenSetup

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
screen_setup_turtle = ScreenSetup()
screen_setup_turtle.setup()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.down, "Down")
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "w")
screen.tracer(True)

game_is_on = True
# game loop
while game_is_on:
    screen.update()

screen.exitonclick()
