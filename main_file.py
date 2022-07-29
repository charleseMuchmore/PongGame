from turtle import Screen
from paddle import Paddle
from screen_setup import ScreenSetup
from ball import Ball
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
    time.sleep(0.04)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        left_player_score += 1
        ball.reset()

    if ball.xcor() < -380:
        right_player_score += 1
        ball.reset()


    #
    # 
    #  if ball.xcor() > 380 or ball.xcor() < -380:
    #     ball.bounce('x')


    



screen.exitonclick()
