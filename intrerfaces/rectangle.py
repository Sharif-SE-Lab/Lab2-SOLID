import interface

LENGTH_TYPE = float


class RectangleInterfaceForTest(interface.Interface):
    def __init__(self, width: LENGTH_TYPE, height: LENGTH_TYPE):
        pass

    def compute_area(self) -> float:
        pass
