LENGTH_TYPE = float


class InvalidLengthException(Exception):
    pass


class Rectangle:
    def __init__(self, width: LENGTH_TYPE, height: LENGTH_TYPE):
        self.__width = width
        self.__height = height

    @staticmethod
    def __validate_length(length: LENGTH_TYPE) -> bool:
        return length > 0

    def compute_area(self) -> LENGTH_TYPE:
        if self.__validate_length(self.__width) and self.__validate_length(
            self.__height
        ):
            return self.__width * self.__height
        return 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: LENGTH_TYPE):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: LENGTH_TYPE):
        self.__height = value
