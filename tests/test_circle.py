import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_valid_construction(self):
        circle = Circle(0, 0, 5)
        self.assertEqual(circle.x_center, 0)
        self.assertEqual(circle.y_center, 0)
        self.assertEqual(circle.radius, 5)

    def test_invalid_zero_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, 0)
    def test_invalid_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -5)
    def test_invalid_nonnumeral_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, "Joshua")

    def test_altering_radius(self):
        circle = Circle(0, 0, 5)
        circle.radius = 10
        self.assertAlmostEqual(circle.area, 314.1592653589793)
    def test_altering_x_center(self):
        circle = Circle(0, 0, 5)
        circle.x_center = 10
        self.assertEqual(circle.area, 0)
    def test_altering_y_center(self):
        circle = Circle(0, 0, 5)
        circle.y_center = 10
        self.assertEqual(circle.area, 0)

    def test_changing_name(self):
        circle = Circle(0, 0, 5)
        circle.name = "New Circle"
        self.assertEqual(circle.name, "New Circle") 

    def test_initial_area(self):
        circle = Circle(0, 0, 3)
        self.assertEqual(circle.area, 0)
    def test_area(self):
        circle = Circle(0, 0, 5)
        self.assertEqual(circle.calc_area(), 78.53981633974483)

if __name__ == "__main__":
    unittest.main()