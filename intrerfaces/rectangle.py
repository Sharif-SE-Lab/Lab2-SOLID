from intrerfaces.shape import Shape, LENGTH_TYPE


class RectangleInterfaceForTest(Shape):
    def __init__(self, width: LENGTH_TYPE, height: LENGTH_TYPE):
        pass

    def compute_area(self) -> LENGTH_TYPE:
        pass

