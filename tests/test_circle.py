import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(0, 0, 5)

    def test_valid_construction(self):
        self.assertEqual(self.circle.x_center, 0)
        self.assertEqual(self.circle.y_center, 0)
        self.assertEqual(self.circle.radius, 5)

    def test_invalid_zero_radius(self):
        with self.assertRaises(ValueError):
            self.circle.radius = 0
    def test_invalid_negative_radius(self):
        with self.assertRaises(ValueError):
            self.circle.radius = -5
    def test_invalid_nonnumeral_radius(self):
        with self.assertRaises(ValueError):
            self.circle.radius = "Joshua"

    def test_altering_radius(self):
        self.circle.radius = 10
        self.assertAlmostEqual(self.circle.area, 314.1592653589793)
    def test_altering_x_center(self):
        self.circle.x_center = 10
        self.assertEqual(self.circle.area, 0)
    def test_altering_y_center(self):
        self.circle.y_center = 10
        self.assertEqual(self.circle.area, 0)

    def test_changing_name(self):
        self.circle.name = "New Circle"
        self.assertEqual(self.circle.name, "New Circle") 

    def test_initial_area(self):
        self.assertEqual(self.circle.area, 0)
    def test_area(self):
        self.assertEqual(self.circle.calc_area(), 78.53981633974483)

if __name__ == "__main__":
    unittest.main()