import unittest

from interfaces.shape import LENGTH_TYPE, InvalidLengthException
from interfaces.square import SquareInterfaceForTest


class TestSquare(unittest.TestCase):

    def create_square(self, side: LENGTH_TYPE) -> 'SquareInterfaceForTest':
        from src.square import Square
        return Square(side=side)

    def test_length_validation(self):
        for invalid_length in [0, -3, -1000]:
            with self.assertRaises(InvalidLengthException):
                self.create_square(side=invalid_length)

        for valid_length in [1, 10, 10000]:
            self.assertIsNotNone(self.create_square(side=valid_length))

    def test_set_side(self):
        square: 'SquareInterfaceForTest' = self.create_square(side=10)
        square.side = 10
        self.assertEqual(square.compute_area(), 10 * 10)

    def test_set_side_failed(self):
        square: 'SquareInterfaceForTest' = self.create_square(side=10)
        for invalid_length in [0, -3, -1000]:
            with self.assertRaises(InvalidLengthException):
                square.side = invalid_length