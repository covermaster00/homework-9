class Stationery:
    title = 'непонятно зачем этот атрибут'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисуем карандашом')

class Pencil(Stationery):
    def draw(self):
        print('Сейчас рисуем ручкой')

class Handle(Stationery):
    def draw(self):
        print('Используем маркер')


[i.draw(i) for i in (Stationery, Pen, Pencil, Handle)]
