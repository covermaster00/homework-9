class Car:
    def __init__(self, color_, name_):
        self.speed, self.color, self.name, self.is_police = 0, color_, name_, False

    def go(self, speed_):
        self.speed = speed_
        print(f'Разгон до скорости {speed_} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Остановлено')

    def turn(self, direction):
        direction = str.lower(direction)
        _ = ['влево', 'вправо', 'налево', 'направо']
        print(f'{"Поворот " + direction if direction in _ else "Направление задано неверно! "}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        print(f'{"Превышение скорости!" if self.speed > 60 else ""} Скорость: {self.speed} км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'{"Превышение скорости!" if self.speed > 40 else ""} Скорость: {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, name_):
        Car.__init__(self, 'спецокрас', name_)
        self.is_police = True


cars = (WorkCar('RED', 'Hyndai'), SportCar('White', 'BMW'), TownCar('Black', 'LADA'), PoliceCar('KIA'))
for i in cars:
    print(f'{i.name} - {"полицейский" if i.is_police else "гражданский"} автомобиль. Цвет: {i.color}')
    i.go(40)
    i.show_speed()
    i.go(50)
    i.show_speed()
    i.turn('НАЛЕВО')
    i.turn('Вправо')
    i.stop()
