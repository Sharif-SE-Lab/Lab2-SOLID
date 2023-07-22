import os
from random import randint
import sys
from typing import Dict, List, Optional
from rectangle import LENGTH_TYPE, InvalidLengthException, Rectangle
import unittest
from abc import ABCMeta, abstractmethod


class RectangleTestCase(unittest.TestCase, metaclass=ABCMeta):
    def __init__(self, parameters: Dict) -> None:
        super().__init__()
        self.parameters = parameters

    def create_rectangle(self) -> "Rectangle":
        return Rectangle(**self.parameters)

    @abstractmethod
    def test_length_validation(self):
        pass

    def next_case_assign(self, rectangle: "Rectangle"):
        rectangle.width = self.parameters["width"]
        rectangle.height = self.parameters["height"]

    @abstractmethod
    def test_set_get(self, base_rectangle: "Rectangle"):
        pass


class InvalidRectangleTestCase(RectangleTestCase):
    def __init__(self, parameters: Dict) -> None:
        super().__init__(parameters)

    def test_length_validation(self):
        self.assertRaises(InvalidLengthException, self.create_rectangle)

    def test_set_get(self, base_rectangle: Rectangle):
        self.assertRaises(
            InvalidLengthException, lambda: self.next_case_assign(base_rectangle)
        )


class ValidRectangleTestCase(RectangleTestCase):
    def __init__(self, parameters: Dict, expected_computed_area: LENGTH_TYPE) -> None:
        super().__init__(parameters)
        self.expected_computed_area = expected_computed_area

    def test_length_validation(self):
        self.create_rectangle()

    def test_set_get(self, base_rectangle: Rectangle):
        self.next_case_assign(base_rectangle)
        self.test_computed_area(base_rectangle)

    def test_computed_area(self, rectangle: Optional["Rectangle"] = None):
        Not_Optional_rectangle: "Rectangle" = (
            self.create_rectangle() if rectangle is None else rectangle
        )
        self.assertEqual(
            Not_Optional_rectangle.compute_area(), self.expected_computed_area
        )

    def test_set_get_transition(self, next_case: "RectangleTestCase"):
        next_case.test_set_get(self.create_rectangle())


class TestRectangle(unittest.TestCase):
    @staticmethod
    def generate_random_index(min_num: int = 0, max_num: int = 0) -> int:
        return randint(min_num, max_num)

    def setUp(self):
        print("\nRunning setUp method...")
        self.tests_num = 13
        self.rectangle_test_cases: List["RectangleTestCase"] = [
            InvalidRectangleTestCase({"width": -3, "height": -5}),
            InvalidRectangleTestCase({"width": -3, "height": -3}),
            InvalidRectangleTestCase({"width": -3, "height": -1}),
            InvalidRectangleTestCase({"width": -5, "height": 0}),
            InvalidRectangleTestCase({"width": -7, "height": 3}),
            InvalidRectangleTestCase({"width": 0, "height": -5}),
            InvalidRectangleTestCase({"width": 0, "height": 0}),
            InvalidRectangleTestCase({"width": 0, "height": 5}),
            InvalidRectangleTestCase({"width": 3, "height": -7}),
            InvalidRectangleTestCase({"width": 5, "height": 0}),
            ValidRectangleTestCase({"width": 6, "height": 4}, 24),
            ValidRectangleTestCase({"width": 7, "height": 7}, 49),
            ValidRectangleTestCase({"width": 5, "height": 8}, 40),
        ]
        self.random_set_gets: List[int] = [
            self.generate_random_index(max_num=self.tests_num - 1)
            for i in range(self.tests_num)
        ]

    def tearDown(self):
        print("Running tearDown method...")

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


if __name__ == "__main__":
    unittest.main()
