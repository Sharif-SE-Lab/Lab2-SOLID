from interfaces.shape import Shape, LENGTH_TYPE


class RectangleInterfaceForTest(Shape):
    def __init__(self, width: LENGTH_TYPE, height: LENGTH_TYPE):
        pass

    def compute_area(self) -> LENGTH_TYPE:
        pass

    @property
    def width(self) -> LENGTH_TYPE:
        pass

    @width.setter
    def width(self, value: LENGTH_TYPE):
        pass

    @property
    def height(self) -> LENGTH_TYPE:
        pass

    @height.setter
    def height(self, value: LENGTH_TYPE):
        pass

