from basic_shape import BasicShape

class Rectangle(BasicShape):
    def __init__(self, width, length):
        if isinstance(width, bool) or not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("Width must be a valid number")
        if isinstance(length, bool) or not isinstance(length, int) and not isinstance(length, float):
            raise TypeError("Length must be a valid number")

        area = width * length
        super().__init__("Rectangle", area)
        self._width = width
        self._length = length
        self.calc_area()

    @property
    def width(self):
        return self._width
    @property
    def length(self):
        return self._length

    @width.setter
    def width(self, value):
        if not isinstance(value, int) and not isinstance(value, float) or value <= 0:
            raise ValueError("Width must be a valid, positive numeral")
        self._width = value
        self.calc_area()
    @length.setter
    def length(self, value):
        if not isinstance(value, int) and not isinstance(value, float) or value <= 0:
            raise ValueError("Length must be a valid, positive numeral")
        self._length = value
        self.calc_area()

    def calc_area(self):
        self._area = self._width * self._length
        return self._area