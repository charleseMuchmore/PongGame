from turtle import Screen
from paddle import Paddle
from screen_setup import ScreenSetup
from ball import Ball
from scoreboard import Scoreboard
import time

UPPER_BORDER = 280
LOWER_BORDER = -280
PADDLE_RADIUS = 50
EDGE_R_PADDLE = 320
EDGE_L_PADDLE = -320
R_GOAL = 380
L_GOAL = -380


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
ball_speed = ball.move_speed
print(type(ball_speed))
# game loop
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > UPPER_BORDER or ball.ycor() < LOWER_BORDER:
        ball.bounce_y()
    if ball.distance(r_paddle) < PADDLE_RADIUS and ball.xcor() > EDGE_R_PADDLE or ball.distance(l_paddle) < PADDLE_RADIUS and ball.xcor() < EDGE_L_PADDLE:
        ball.bounce_x()
    if ball.xcor() > R_GOAL:
        scoreboard.l_point()
        ball.reset()
        ball.speed_reset()
    if ball.xcor() < L_GOAL:
        scoreboard.r_point()
        right_player_score += 1
        ball.reset()



screen.exitonclick()
