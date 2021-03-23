class Worker:
    def __init__(self, n, s, p='разнорабочий', i_w=20000, i_b=5000):
        try:
            self.name = str.capitalize(n)
            self.surname = str.capitalize(s)
            self.position = str.lower(p)
            self._income = {'wage': int(i_w), 'bonus': int(i_b)}
        except:
            print('Данные указаны некорректно')

class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self, m):

        def homework1_1(procent):
            if procent % 10 == 1 and procent % 100 != 11:
                return ""
            elif 1 < procent % 10 < 5 and not 11 < procent % 100 < 15:
                return "а"
            else:
                return "ев"

        print(f'Доход за {m} месяц{homework1_1(m)} с учетом годовой премии: '
              f'{m * self._income["wage"] + self._income["bonus"] * (m // 12)} руб')


pos = (Position('ИВАНОВ', 'иван', 'маляр', 3000, 1000), Position('петров', 'максим', 'сторож', 2500, 800),
       Position('васильев', 'николай'), Position('криворогов', 'арбуз'))
from random import randint
[(i.get_full_name(), i.get_total_income(randint(1, 50))) for i in pos]
