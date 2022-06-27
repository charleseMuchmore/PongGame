from paddle import Paddle

class UserPaddle(Paddle):

    def __init__(self):
        super().__init__()

    def up(self):
        self.move(self.MOVE_UP)

    def down(self):
        self.move(self.MOVE_DOWN)
