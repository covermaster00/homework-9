class Road:
    def __init__(self, l, w):
        self._length, self._width = l, w

    def asphalt(self, weight=25, height=5):
        return self._length * self._width * weight * height / 1000

r = Road(20, 5000)
print(f'{r.asphalt()} т.')