import interface

from interfaces.rectangle import RectangleInterfaceForTest
from interfaces.shape import LENGTH_TYPE, Shape, validate_length


class Rectangle(interface.implements(Shape, RectangleInterfaceForTest)):
    def __init__(self, width: LENGTH_TYPE, height: LENGTH_TYPE):
        self._width = width
        self._height = height

    def compute_area(self) -> LENGTH_TYPE:
        return self.width * self.height

    @property
    def width(self) -> LENGTH_TYPE:
        return self._width

    @width.setter
    def width(self, value: LENGTH_TYPE):
        validate_length(value)
        self._width = value

    @property
    def height(self) -> LENGTH_TYPE:
        return self._height

    @height.setter
    def height(self, value: LENGTH_TYPE):
        validate_length(value)
        self._height = value
