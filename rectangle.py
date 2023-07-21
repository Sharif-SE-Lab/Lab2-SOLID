LENGTH_TYPE = float


class Rectangle:
    def __init__(self, width: LENGTH_TYPE, height: LENGTH_TYPE):
        self.width = width
        self.height = height

    @staticmethod
    def __validate_length__(length: LENGTH_TYPE) -> bool:
        return length > 0

    def compute_area(self) -> LENGTH_TYPE:
        if self.__validate_length__(self.width) and self.__validate_length__(self.height):
            return self.width * self.height
        return 0
