from Tasks.shape import Shape


class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def color(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def area(self):
        return self._width * self._length
