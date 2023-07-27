import unittest
from abc import abstractmethod, ABC
from random import randint
from typing import Dict, List, Optional

from interfaces.rectangle import RectangleInterfaceForTest
from interfaces.shape import InvalidLengthException
from src.rectangle import LENGTH_TYPE


class RectangleTestCase(ABC):
    def __init__(self, asserter: unittest.TestCase, parameters: Dict) -> None:
        self.parameters = parameters
        self.asserter = asserter

    def create_rectangle(self) -> 'RectangleInterfaceForTest':
        from src.rectangle import Rectangle
        return Rectangle(**self.parameters)

    @abstractmethod
    def test_length_validation(self):
        pass

    def next_case_assign(self, rectangle: 'RectangleInterfaceForTest'):
        rectangle.width = self.parameters["width"]
        rectangle.height = self.parameters["height"]

    @abstractmethod
    def test_set_get(self, base_rectangle: 'RectangleInterfaceForTest'):
        pass


class InvalidRectangleTestCase(RectangleTestCase):

    def test_length_validation(self):
        self.asserter.assertRaises(InvalidLengthException, self.create_rectangle)

    def test_set_get(self, base_rectangle: 'RectangleInterfaceForTest'):
        self.asserter.assertRaises(
            InvalidLengthException, lambda: self.next_case_assign(base_rectangle)
        )


class ValidRectangleTestCase(RectangleTestCase):
    def __init__(self, asserter: unittest.TestCase, parameters: Dict, expected_computed_area: LENGTH_TYPE) -> None:
        super().__init__(asserter, parameters)
        self.expected_computed_area = expected_computed_area

    def test_length_validation(self):
        self.create_rectangle()

    def test_set_get(self, base_rectangle: 'RectangleInterfaceForTest'):
        self.next_case_assign(base_rectangle)
        self.test_computed_area(base_rectangle)

    def test_computed_area(self, rectangle: Optional['RectangleInterfaceForTest'] = None):
        Not_Optional_rectangle: 'RectangleInterfaceForTest' = (
            self.create_rectangle() if rectangle is None else rectangle
        )
        self.asserter.assertEqual(
            Not_Optional_rectangle.compute_area(), self.expected_computed_area
        )

    def test_set_get_transition(self, next_case: "RectangleTestCase"):
        next_case.test_set_get(self.create_rectangle())


class TestRectangle(unittest.TestCase):
    @staticmethod
    def generate_random_index(min_num: int = 0, max_num: int = 0) -> int:
        return randint(min_num, max_num)

    invalid_test_cases = [
        ({"width": -3, "height": -5},),
        ({"width": -3, "height": -3},),
        ({"width": -3, "height": -1},),
        ({"width": -5, "height": 0},),
        ({"width": -7, "height": 3},),
        ({"width": 0, "height": -5},),
        ({"width": 0, "height": 0},),
        ({"width": 0, "height": 5},),
        ({"width": 3, "height": -7},),
        ({"width": 5, "height": 0},),
    ]

    valid_test_cases = [
        ({"width": 6, "height": 4}, 24),
        ({"width": 7, "height": 7}, 49),
        ({"width": 5, "height": 8}, 40),
    ]

    def setUp(self):
        print("\nRunning setUp method...")
        self.tests_num = 13
        self.rectangle_test_cases: List["RectangleTestCase"] = []
        for invalid_tc in self.invalid_test_cases:
            self.rectangle_test_cases.append(InvalidRectangleTestCase(self, *invalid_tc))
        for valid_tc in self.valid_test_cases:
            self.rectangle_test_cases.append(ValidRectangleTestCase(self, *valid_tc))
        self.random_set_gets: List[int] = [
            self.generate_random_index(max_num=self.tests_num - 1)
            for i in range(self.tests_num)
        ]

    def test_length_validation(self):
        for i in range(self.tests_num):
            self.rectangle_test_cases[i].test_length_validation()

    def test_computed_area(self):
        print("Running test_computed_area...")
        for i in range(self.tests_num):
            if isinstance(self.rectangle_test_cases[i], ValidRectangleTestCase):
                self.rectangle_test_cases[i].test_computed_area()

    def test_set_get_width_height(self):
        print("Running test_set_get_width_height...")
        for i in range(self.tests_num):
            if isinstance(self.rectangle_test_cases[i], ValidRectangleTestCase):
                self.rectangle_test_cases[i].test_set_get_transition(
                    self.rectangle_test_cases[self.random_set_gets[i]]
                )
