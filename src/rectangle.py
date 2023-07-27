import interface

from intrerfaces.rectangle import RectangleInterfaceForTest, LENGTH_TYPE


class InvalidLengthException(Exception):
    pass


class Rectangle(interface.implements(RectangleInterfaceForTest)):
    def __init__(self, width: LENGTH_TYPE, height: LENGTH_TYPE):
        self.width = width
        self.height = height

    @staticmethod
    def __validate_length(length: LENGTH_TYPE) -> None:
        if length <= 0:
            raise InvalidLengthException

    def compute_area(self) -> LENGTH_TYPE:
        return self.width * self.height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: LENGTH_TYPE):
        self.__validate_length(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: LENGTH_TYPE):
        self.__validate_length(value)
        self.__height = value
