from turtle import Turtle


class ScreenSetup:

    def __init__(self):
        self.screen_setup_turtle = Turtle()
        self.screen_setup_turtle.color("white")
        self.screen_setup_turtle.penup()
        self.screen_setup_turtle.goto(0, 400)
        self.screen_setup_turtle.setheading(270)
        self.screen_setup_turtle.pensize(5)

    def setup(self):
        for x in range(27):
            self.screen_setup_turtle.pendown()
            self.screen_setup_turtle.forward(10)
            self.screen_setup_turtle.penup()
            self.screen_setup_turtle.forward(20)
