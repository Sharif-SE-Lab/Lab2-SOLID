from random import randint
from typing import Dict, List
from rectangle import LENGTH_TYPE, InvalidLengthException, Rectangle
import unittest


class TestBook(unittest.TestCase):
    @staticmethod
    def generate_random_index(min_num: int = 0, max_num: int = 0) -> int:
        return randint(min_num, max_num)

    def setUp(self):
        print("\nRunning setUp method...")
        self.tests_num = 13
        self.rectangle_cases: List[Dict] = [
            {"width": -3, "height": -5},
            {"width": -3, "height": -3},
            {"width": -3, "height": -1},
            {"width": -5, "height": 0},
            {"width": -7, "height": 3},
            {"width": 0, "height": -5},
            {"width": 0, "height": 0},
            {"width": 0, "height": 5},
            {"width": 3, "height": -7},
            {"width": 5, "height": 0},
            {"width": 6, "height": 4},
            {"width": 7, "height": 7},
            {"width": 5, "height": 8},
        ]
        self.rectangle_exceptions = [
            InvalidLengthException,
            InvalidLengthException,
            InvalidLengthException,
            InvalidLengthException,
            InvalidLengthException,
            InvalidLengthException,
            InvalidLengthException,
            InvalidLengthException,
            InvalidLengthException,
            InvalidLengthException,
            None,
            None,
            None,
        ]
        self.rectangle_computed_areas: List[LENGTH_TYPE] = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            24,
            49,
            40,
        ]
        self.random_set_gets: List[int] = [
            self.generate_random_index(max_num=self.tests_num - 1)
            for i in range(self.tests_num)
        ]

    def tearDown(self):
        print("Running tearDown method...")

    def test_length_validation(self):
        for i in range(self.tests_num):
            if self.rectangle_exceptions[i] is not None:
                self.assertRaises(
                    InvalidLengthException, lambda: Rectangle(**self.rectangle_cases[i])
                )
            else:
                Rectangle(**self.rectangle_cases[i])

    def test_computed_area(self):
        print("Running test_computed_area...")
        for i in range(self.tests_num):
            if self.rectangle_exceptions[i] is None:
                rectangle = Rectangle(**self.rectangle_cases[i])
                self.assertEqual(
                    rectangle.compute_area(), self.rectangle_computed_areas[i]
                )

    def test_set_get_width_height(self):
        print("Running test_set_get_width_height...")
        for i in range(self.tests_num):
            if self.rectangle_exceptions[i] is None:
                rectangle = Rectangle(**self.rectangle_cases[i])
                next_i = self.random_set_gets[i]
                next_i_case = self.rectangle_cases[next_i]

                def next_case_assign():
                    rectangle.width = next_i_case["width"]
                    rectangle.height = next_i_case["height"]

                if self.rectangle_exceptions[next_i] is None:
                    next_case_assign()
                    next_i_computed_area = self.rectangle_computed_areas[next_i]
                    self.assertEqual(rectangle.compute_area(), next_i_computed_area)
                else:
                    self.assertRaises(InvalidLengthException, next_case_assign)


if __name__ == "__main__":
    unittest.main()
