import unittest
from typing import List

import interface

from interfaces.shape import Shape


class TestableShapeInterface(interface.Interface):

    @property
    def actual_area(self) -> float:
        pass

    @property
    def expected_area(self) -> float:
        pass


class ShapeTestAdapter(interface.implements(TestableShapeInterface)):
    _shape: Shape

    def __init__(self, shape: Shape, expected_area: float):
        self._shape = shape
        self._expected_area = expected_area

    @property
    def actual_area(self) -> float:
        return self._shape.compute_area()

    @property
    def expected_area(self) -> float:
        return self._expected_area


class TestShape(unittest.TestCase):

    def get_testable_shapes(self) -> List['TestableShapeInterface']:
        testable_shapes: List[TestableShapeInterface] = []
        for side in [12, 23, 1, 2.5]:
            from src.square import Square
            testable_shapes.append(ShapeTestAdapter(Square(side=side), expected_area=side * side))
        for w, h in [(1, 3), (0.5, 9), (4, 1)]:
            from src.rectangle import Rectangle
            testable_shapes.append(ShapeTestAdapter(Rectangle(w, h), expected_area=w * h))
        return testable_shapes

    def test_expected_areas(self):
        for testable_shape in self.get_testable_shapes():
            self.assertEqual(testable_shape.actual_area, testable_shape.expected_area)
