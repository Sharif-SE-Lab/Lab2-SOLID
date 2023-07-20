from typing import List
from rectangle import LENGTH_TYPE, Rectangle
import unittest


class TestBook(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        self.tests_num = 0
        self.rectangles: List[Rectangle] = []
        self.rectangle_computed_areas: List[LENGTH_TYPE] = []

    def tearDown(self):
        print("Running tearDown method...")

    def test_computed_area(self):
        print("Running test_reading_time...")
        for i in range(self.tests_num):
            self.assertEquals(
                self.rectangles[i].compute_area(), self.rectangle_computed_areas[i]
            )


if __name__ == "__main__":
    unittest.main()
