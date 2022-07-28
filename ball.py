from re import U
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.position = self.pos()

        

    def move(self):
        y = self.determine_y_movement_direction()
        x = self.determine_x_movement_direction()
        new_x = self.xcor() + x
        new_y = self.ycor() + y
        self.goto(new_x, new_y)


    def determine_y_movement_direction(self):
        ycollision = self.detect_collision(290, self.ycor())
        if ycollision == True:
            if self.ycor() >= 0:
                return(-10)
            elif self.ycor() <= 0:
                return(+10)
            else:
                print ("error")
        elif ycollision == False:
            if self.ycor() >= 0:
                return(+10)
            elif self.ycor() <= 0:
                return(-10)
            else:
                print ("error")
        else:
            print ("error")

    def determine_x_movement_direction(self):
        xcollision = self.detect_collision(390, self.xcor())
        if xcollision == True:
            if self.xcor() >= 0:
                return(-10)
            elif self.xcor() <= 0:
                return(+10)
            else:
                print ("error")
        elif xcollision == False:
            if self.xcor() > -1:
                return(+10)
            elif self.xcor() < 1 :
                return(-10)
            else:
                print ("error")
        else:
            print("error")

    def detect_collision(self, limit, cortype):
        if cortype >= limit or cortype <= -limit:
            return True
        elif cortype < limit and cortype > -limit:
            return False
