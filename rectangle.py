from basic_shape import BasicShape

class Rectangle(BasicShape):
    def __init__(self, _width, _length):
        self._width = width
        self._length = length
        if not isinstance(_radius, int) and not isinstance(_radius, float) or _radius <= 0:
            raise ValueError("Radius must be a valid positive numeral")
        self._radius = _radius
        super().__init__("Circle", math.pi * _radius ** 2)