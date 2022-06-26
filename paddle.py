from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_pieces = []

    def create_paddle(self, paddle_size, paddle_color):
        """this method adds turtle pieces of a paddle to a list"""
        for x in range(paddle_size):
            x = Turtle("square")
            x.color(paddle_color)
            x.penup()
            x.speed("fastest")
            self.paddle_pieces.append(x)

    def center_paddle(self, xcoor):
        """centers the paddle along the x axis at the given xcoor"""
        middle_index = self.find_middle(self.paddle_pieces)
        if type(middle_index) != tuple:
            for item in self.paddle_pieces:
                item_index = self.paddle_pieces.index(item)
                ycoor = (middle_index - item_index) * 20
                item.goto(xcoor, ycoor)
        elif len(middle_index) == 2:
            for item in self.paddle_pieces:
                upper_index = middle_index[0]
                lower_index = middle_index[1]
                item_index = self.paddle_pieces.index(item)
                if item_index <= upper_index:
                    ycoor = (upper_index - item_index) * 20 + 10
                elif item_index >= upper_index:
                    ycoor = (lower_index - item_index) * 20 - 10
                item.goto(xcoor, ycoor)


    def find_middle(self, input_list):
        """finds the center of a list, returns a single integer that correlates to
        the central index if odd, and two integers if list is even"""
        middle_num = float(len(input_list))/2
        if len(input_list) % 2 != 0:
            return int(middle_num)
        else:
            return int(middle_num - 0.5), int(middle_num + 0.5)