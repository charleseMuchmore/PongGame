from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmover = +10
        self.ymover = +10
        self.move_speed = 0.04

    def move(self):
        new_x = self.xcor() + self.xmover
        new_y = self.ycor() + self.ymover
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymover *= -1
        
    def bounce_x(self):
        self.xmover *= -1

    def reset(self):
        self.hideturtle()
        self.goto(0,0)
        self.bounce_x()
        self.showturtle()

    def speed_reset(self):
        self.move_speed = 0.04 
