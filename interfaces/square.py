from interfaces.shape import Shape, LENGTH_TYPE


class SquareInterfaceForTest(Shape):

    def __init__(self, side: LENGTH_TYPE):
        pass

    @property
    def side(self):
        pass

    @side.setter
    def side(self, value: LENGTH_TYPE):
        pass
