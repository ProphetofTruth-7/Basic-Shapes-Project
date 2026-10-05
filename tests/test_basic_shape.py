import unittest
from basic_shape import BasicShape

class SampleShape(BasicShape):
    def __init__(self, name, value=1.0):
        super().__init__(name, value)
        self._value = value
        self.calc_area()
    def calc_area(self):
        self._area = self._value
        return self._area

class TestBasicShape(unittest.TestCase):

    def test_direct_instantiation(self):
        with self.assertRaises(TypeError):
            shape = BasicShape("Shape", 10)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            shape = SampleShape(123, 10)

if __name__ == "__main__":
    unittest.main()