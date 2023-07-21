from random import randint
from typing import Dict, List
from rectangle import LENGTH_TYPE, Rectangle
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

    @property
    def rectangles(self) -> List[Rectangle]:
        return [Rectangle(**rectangle_case) for rectangle_case in self.rectangle_cases]

    def tearDown(self):
        print("Running tearDown method...")

    def test_computed_area(self):
        print("Running test_computed_area...")
        rectangles = self.rectangles
        for i in range(self.tests_num):
            self.assertEqual(
                rectangles[i].compute_area(), self.rectangle_computed_areas[i]
            )

    def test_set_get_width_height(self):
        print("Running test_set_get_width_height...")
        rectangles = self.rectangles
        for i in range(self.tests_num):
            i_next_case = self.rectangle_cases[self.random_set_gets[i]]
            i_next_expected_computed_area = self.rectangle_computed_areas[
                self.random_set_gets[i]
            ]
            rectangles[i].width = i_next_case["width"]
            rectangles[i].height = i_next_case["height"]
            self.assertEqual(
                rectangles[i].compute_area(), i_next_expected_computed_area
            )


if __name__ == "__main__":
    unittest.main()
