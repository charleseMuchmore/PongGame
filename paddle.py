from turtle import Turtle
# STARTING_POSITIONS = [(-300, 40), (-300, 20), (-300, 0), (-300, -20), (-300, -40)]


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_pieces = []
        # self.create_paddle()
        # self.position_paddle()

    def create_paddle(self, paddle_size, paddle_color):
        """self, int, string. this method adds turtle pieces of a paddle to a list"""
        for x in range(paddle_size):
            x = Turtle("square")
            x.color(paddle_color)
            x.penup()
            self.paddle_pieces.append(x)


    def position_paddle(self, xcoor):
        middle_index = self.find_middle(self.paddle_pieces)
        print(f"middle: {middle_index}")
        if type(middle_index) != tuple:
            for item in self.paddle_pieces:
                item_index = self.paddle_pieces.index(item)
                ycoor = (item_index - middle_index) * -20
                item.goto(xcoor, ycoor)

        # elif len(middle_index) == 2:
        #     self.paddle_pieces[middle_index[0]].goto(xcoor, 0 + 10)
        #     self.paddle_pieces[middle_index[1]].goto(xcoor, 0 - 10)

    def find_middle(self, input_list):
        """finds the center of a list, returns a single integer that correlates to
        the central index if odd, and two integers if list is even"""
        middle_num = float(len(input_list))/2
        if middle_num % 2 != 0:
            print(f"its odd: {int(middle_num)}")
            return int(middle_num)
        else:
            print(f"its even: {(int(middle_num - 0.5), int(middle_num + 0.5))}")
            return int(middle_num - 0.5), int(middle_num + 0.5)

    # def position_paddle(self):
    #     times_thru = 0
    #     for item in STARTING_POSITIONS:
    #         paddle_item = self.paddle_pieces[times_thru]
    #         paddle_item.goto(item)
    #         times_thru += 1



    def print_paddle_pieces(self):
        """prints the list of turtle objects that make up the user paddle"""
        print(f"turd list: {self.paddle_pieces}")