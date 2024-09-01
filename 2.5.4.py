class Square:
    def __init__(self, side):
        self.side = side

class SquareFactory:
    @staticmethod
    def square_gen(side):
        return Square(side)
