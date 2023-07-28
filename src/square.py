import interface

from interfaces.shape import Shape, LENGTH_TYPE, validate_length
from interfaces.square import SquareInterfaceForTest


class Square(interface.implements(Shape, SquareInterfaceForTest)):

    def __init__(self, side: LENGTH_TYPE):
        self.side = side

    def compute_area(self) -> LENGTH_TYPE:
        return self.side ** 2

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value: LENGTH_TYPE):
        validate_length(value)
        self._side = value
