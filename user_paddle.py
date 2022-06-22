from turtle import Turtle
STARTING_POSITIONS = [(-300, 40), (-300, 20), (-300, 0), (-300, -20), (-300, -40)]
NUM_PADDLE_PIECES = 5


class UserPaddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_pieces = []
        self.create_paddle()
        self.position_paddle()

    def position_paddle(self):
        times_thru = 0
        for item in STARTING_POSITIONS:
            paddle_item = self.paddle_pieces[times_thru]
            paddle_item.goto(item)
            times_thru += 1

    def create_paddle(self):
        for x in range(NUM_PADDLE_PIECES):
            x = Turtle("square")
            x.color("white")
            x.penup()
            self.paddle_pieces.append(x)


    def print_paddle_pieces(self):
        """prints the list of turtle objects that make up the user paddle"""
        print(f"turd list: {self.paddle_pieces}")
