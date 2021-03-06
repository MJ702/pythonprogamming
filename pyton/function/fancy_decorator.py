class Square:

    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, values):
        if values >= 0:
            self._side = values
        else:
            print("error")

    @property
    def area(self):
        return self._side ** 2

    @classmethod
    def unit_square(cls):
        return cls(1)


s = Square(5)

print(s.side)
print(s.area)
