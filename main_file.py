from turtle import Screen
from paddle import Paddle
from screen_setup import ScreenSetup
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
screen_setup_turtle = ScreenSetup()
screen_setup_turtle.setup()
screen_setup_turtle.draw_border()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.down, "Down")
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "w")
screen.tracer(True)

left_player_score = 0
right_player_score = 0
game_is_on = True
# game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # wall bounce logic
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # paddle bounce logic
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # points logic
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
    if ball.xcor() < -380:
        scoreboard.r_point()
        right_player_score += 1
        ball.reset()


    #
    # 
    #  if ball.xcor() > 380 or ball.xcor() < -380:
    #     ball.bounce('x')


    



screen.exitonclick()
