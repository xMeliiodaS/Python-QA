from Tasks.shape import Shape
from math import pi


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def area(self):
        return self._radius ** 2 * pi