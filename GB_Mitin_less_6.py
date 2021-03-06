'''
Практическое задание
1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
(ширина). Значения данных атрибутов должны передаваться при создании экземпляра
класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
(TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
'''
'''
1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
'''
import time

class c_TrafficLight:
    __color = None
    modes = [
       {'color': 'Red',     'time': 7},
       {'color': 'Yellow',  'time': 2},
       {'color': 'Green',   'time': 5}
    ]

    def __init__(self):
        self.is_start_new_mode = False
        self.elapsed_time = 0
        self.indx       = 0

    def Running(self, seconds):
        if self.is_start_new_mode is False:
            self.__color = self.modes[self.indx]['color']
            self.elapsed_time = seconds + self.modes[self.indx]['time']
            self.indx += 1
            self.indx %= len(self.modes)
            self.is_start_new_mode = True
        else:
            if seconds >= self.elapsed_time:
                self.is_start_new_mode = False
        print(f' TrafficLight color:  {self.__color} the time remaining: {self.elapsed_time - seconds} sec')



def Test_TrafficLight_Obj( test_time_sec, obj ):
    elapsed = time.time()
    seconds = 0
    while seconds < test_time_sec:
        if time.time() - elapsed >= 1:
            elapsed = time.time()
            seconds += 1
            obj.Running(seconds)
            print(f'the time remaining:: {test_time_sec - seconds} sec')



obj = c_TrafficLight()
#Test_TrafficLight_Obj( 60, obj )

'''
2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
(ширина). Значения данных атрибутов должны передаваться при создании экземпляра
класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''
class c_Road:
    _length = None
    _width  = None
    ''' Плотность асфальта находится в диапазоне 1300 – 1700 кг/м3, 
        для асфальтобетона – в диапазоне 2100 – 2700 кг/м3.
        задаемся 2500кг/м3
    '''
    ASPHALT_DENSITY_KG_M3 = 2500

    def __init__(self, lengh_m, width_m):
        self._length = lengh_m
        self._width = width_m

    def get_lengh(self):
        return self._length

    def get_width(self):
        return self._width

    def get_asphalt_mass(self, thikness_cm):
        return self._length*self._width*(thikness_cm/100) * self.ASPHALT_DENSITY_KG_M3

tst_c_Road = c_Road(1,1)
print(f'Масса асфальта= {tst_c_Road.get_asphalt_mass(100)} кг, '
      f'необходимого для покрытия дорожного полотна: длина= {tst_c_Road.get_lengh()}м, ширина= {tst_c_Road.get_width()}м, толщина= {100}см')
assert tst_c_Road.get_asphalt_mass(100) == c_Road.ASPHALT_DENSITY_KG_M3

'''
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
'''
class c_Worker:
    name = None
    surname = None
    position = None
    _income = {'wage':0, 'bonus':0}

    def __init__(self, name, surname, positon, income):
        self.name = name
        self.surname = surname
        self.position = positon
        self._income = income

    def get_full_name(self):
        return ''.join([self.name, ' ', self.surname])

    def get_total_income(self):
        return self._income['wage'] +self._income['bonus']

class c_Position(c_Worker):
    def __init__(self, name, surname, positon, income):
        super().__init__(name, surname, positon, income)

Worker_Petroff = c_Position( 'Вадим', 'Петрофф', 'инженер-программист', {'wage':100000, 'bonus':60000} )
print(f'ФИО: {Worker_Petroff.get_full_name()}, доход: {Worker_Petroff.get_total_income()}' )

'''
4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
(TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''
class c_Base_Car:
    speed = None
    color = None
    name = None
    is_police = None
    direction_val = ('прямо', 'налево', 'направо', 'в обратном направлении')

    def __init__(self, name, color, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = 'прямо'
        self.speed = 0

    def go(self, speed, direction):
        action = f'машина {self.name} поехала'
        self.speed = speed
        self.direction = direction
        return action

    def stop(self):
        action = f'машина {self.name} остановилась'
        self.speed = 0
        return action

    def turn(self, direction):
        action = f'машина {self.name} повернула {direction}'
        return action

    def show_speed(self):
        return f'Скорость {self.name}: {self.speed} км/час'

class c_SportCar(c_Base_Car):
    def __init__(self, name, color):
        super().__init__(name, color)

class c_PoliceCar(c_Base_Car):
    def __init__(self, name, color):
        super().__init__(name, color, True)

class c_TownCar(c_Base_Car):
    speed_up_limit = None

    def __init__(self, name, color):
        super().__init__(name, color)
        self.speed_up_limit = 40

    def show_speed(self):
        msg = ''
        if self.speed > self.speed_up_limit:
            msg = f' Зафиксировано превышение скорости {self.name} на {round(self.speed-self.speed_up_limit,1)} км/час'
        return f' Машина {self.name} цвет: { self.color} скорость: {self.speed} км/час.{msg}'

class c_WorkCar(c_TownCar):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.speed_up_limit = 60

import random
list_of_cars = [ c_SportCar( 'Super_SportCar', 'черный'),
                 c_WorkCar( 'WorkCar_Truck', 'брызги шампанского'),
                 c_TownCar( 'TownCar_Truck', 'синий'),
                 c_PoliceCar( 'Super_PoliceCar', 'черный')
]
for car in list_of_cars:
    print( car.go(random.randint(50, 201), 'прямо'))
    print( car.show_speed())
    print( car.go(random.randint(20, 80), 'налево'))
    print( car.show_speed())
    print( car.go(random.randint(20, 80), 'направо'))
    print( car.show_speed())
    print( car.go(random.randint(50, 201), 'прямо'))
    print( car.show_speed())
    print( car.stop())

'''
5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
'''
class c_Stationery:
    title = None
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'{self.title} запуск отрисовки.')

class c_Pen(c_Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('class c_Pen (ручка).')

class c_Pencil(c_Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('class c_Pencil (карандаш)')
        super().draw()

class c_Handle(c_Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('class c_Handle (маркер).')
        super().draw()


list_of_Stationery = [ c_Pen('Синяя ручка'),
                       c_Pencil('Черный карандаш'),
                       c_Handle('Зеленый маркер'),
                       c_Handle('Красный маркер')]

for Stationery in list_of_Stationery:
    Stationery.draw()

