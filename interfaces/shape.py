import interface


class InvalidLengthException(Exception):
    pass


LENGTH_TYPE = float


def validate_length(length: LENGTH_TYPE) -> None:
    if length <= 0:
        raise InvalidLengthException


class Shape(interface.Interface):

    def compute_area(self) -> float:
        pass
