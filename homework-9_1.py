from time import sleep

class TrafficLight:
    _color = {1: ['Red', 7, "\033[31m{}"], 2: ['Yellow', 2, "\033[33m{}"], 3: ['Green', 7, "\033[32m{}"]}
    gen = (i for i in _color)

    def luminate(self):

        def blink():
            id = next(self.gen)
            print(self._color[id][2].format(f'{self._color[id][0]} for {self._color[id][1]} second'))
            sleep(self._color[id][1])

        try:
            blink()
        except StopIteration:
            self.gen = (i for i in self._color)
            blink()


# При любом количестве дальнейших вызовов luminate порядок срабатываний светофора не нарушится
crossroad = TrafficLight()
[crossroad.luminate() for i in range(10)]

