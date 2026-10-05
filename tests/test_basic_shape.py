import unittest
from basic_shape import BasicShape

class TestBasicShape(unittest.TestCase):

    def test_direct_instantiation(self):
        with self.assertRaises(TypeError):
            shape = BasicShape("Shape", 10)

if __name__ == "__main__":
    unittest.main()