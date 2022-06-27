from turtle import Turtle


class Paddle(Turtle):
    MOVE_UP = "up"
    MOVE_DOWN = "down"

    def __init__(self):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.resizemode(rmode="user")
        self.paddle.seth(90)
        self.paddle.shapesize(stretch_len=10)
        self.paddle.goto(-350, 0)
        self.paddle.color("white")
        self.paddle.penup()

    def move(self, direction):
        if direction == self.MOVE_DOWN:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)
        if direction == self.MOVE_UP:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)


