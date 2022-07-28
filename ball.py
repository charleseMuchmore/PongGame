from re import U
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.position = self.pos()
        self.xmover = +10
        self.ymover = +10

    def move(self):
        # y = self.determine_y_movement_direction()
        # x = self.determine_x_movement_direction()
        new_x = self.xcor() + self.xmover
        new_y = self.ycor() + self.ymover
        self.goto(new_x, new_y)

    def bounce(self, coordinate):
        if coordinate == 'y':
            self.ymover = self.ymover * -1
        elif coordinate == 'x':
            self.xmover = self.xmover * -1
        else:
            print("there has been a bouncing error")
        