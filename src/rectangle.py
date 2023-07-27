import interface

from interfaces.rectangle import RectangleInterfaceForTest
from interfaces.shape import LENGTH_TYPE, Shape, validate_length


class Rectangle(interface.implements(Shape, RectangleInterfaceForTest)):
    def __init__(self, width: LENGTH_TYPE, height: LENGTH_TYPE):
        self._width, self._height = None, None
        self.width = width
        self.height = height

    def compute_area(self) -> LENGTH_TYPE:
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: LENGTH_TYPE):
        validate_length(value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: LENGTH_TYPE):
        validate_length(value)
        self._height = value
