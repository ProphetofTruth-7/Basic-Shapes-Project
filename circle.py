from basic_shape import BasicShape
import math

class Circle(BasicShape):
    def __init__(self, _x_center, _y_center, _radius):
        self._x_center = _x_center
        self._y_center = _y_center
        self._radius = _radius
        super().__init__("Circle", math.pi * _radius ** 2)

    @property
    def x_center(self):
        return self._x_center
    @property
    def y_center(self):
        return self._y_center
    @property
    def radius(self):
        return self._radius

    @x_center.setter
    def x_center(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError("x_center must be a valid numeral")
        self._x_center = value

    @y_center.setter
    def y_center(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError("y_center must be a valid numeral")
        self._y_center = value

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int) and not isinstance(value, float) or value <= 0:
            raise ValueError("Radius must be a valid positive numeral")
        self._radius = value
        self.calc_area()
    
    def calc_area(self):
        self._area = math.pi * self._radius **2
        return self._area
    