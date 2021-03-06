'''
Практическое задание
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.

3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****.
'''

'''
1) Реализовать класс Matrix (матрица матрица — система некоторых математических величин, 
расположенных в виде прямоугольной схемы). 
Обеспечить перегрузку конструктора класса (метод __init__()), который должен 
принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
реализовать перегрузку метода __add__() для реализации операции сложения двух объектов 
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
class c_Matrix:
    matrix_data = []
    # определим число столбцовб или элементов в строке
    el_in_row = 0
    rows = 0

    def __init__(self, data):
        if type(data) is type(list()):
            self.matrix_data = data
        self.rows = len(data)
        if self.rows:
            row_lens = []
            for row in self.matrix_data:
                row_lens.append(len(row))
            self.el_in_row = max(row_lens)
            for row in self.matrix_data:
                len_of_row = len(row)
                if len_of_row < self.el_in_row:
                    for indx in range(self.el_in_row - len_of_row ):
                        row.append(None)

    def __str__(self):
        res = f'class c_Matrix: rows = {self.rows}, el_in_row = {self.el_in_row}\n'
        for row in self.matrix_data:
            for el in row:
                res += ''.join( [str(el), ' '] )
            res += '\n'
        return res

    def __add__(self, matrix):
        result = []

        # Складываем матрицы только одинаковых размерностей иначе бросим иключение...
        if self.rows == matrix.rows and self.el_in_row == matrix.el_in_row:
            for row in range(self.rows):
                sum_list = [ a + b for a, b in zip(self.matrix_data[row], matrix.matrix_data[row])]
                result.append( sum_list )
        else:
            raise ValueError
        return c_Matrix(result)

matrix_a = c_Matrix([[3,4,5],[6,5,4]])
matrix_ax = c_Matrix([[1,2,3],[4,5,6]])
print(f'{matrix_a} + \n{matrix_ax} = \n{matrix_a + matrix_ax}')

'''
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class c_Clothe:
    _clothe_name = None

    def __init__(self, name):
        self._clothe_name = name
#        print(f'class c_Clothe __init__(self, {self._clothe_name})')

    @abstractmethod
    def ClotheConsumption(self):
        pass

    @abstractmethod
    def ClotheConsumption(self):
        pass

    @abstractmethod
    def Info(self):
        pass

class c_Coat(c_Clothe):
    Size = None

    def __init__(self, name, Size):
        super().__init__(name)
        self.Size = Size

    def __str__(self):
        res = f'Пальто {self._clothe_name.lower()}, размер: {self.Size} '
        return res

    @property
    def Info(self):
        return f'Пальто {self._clothe_name.lower()}, размер: {self.Size} '

    def ClotheConsumption(self):
        return round((self.Size/6.5 + 0.5), 1 )


class c_Costume(c_Clothe):
    Heght = None

    def __init__(self, name, Heght):
        super().__init__(name)
        self.Heght = Heght

    def __str__(self):
        res = f'Костюм {self._clothe_name.lower()}, рост: {self.Heght} '
        return res

    @property
    def Info(self):
        return f'Костюм {self._clothe_name.lower()}, рост: {self.Heght} '

    def ClotheConsumption(self):
        return round((2 * self.Heght + 0.3), 1)


Clothe_list = [ c_Costume('Мужской', 1.8),
                c_Costume('Женский', 1.6),
                c_Coat('Детское', 30),
                c_Coat('Женское', 46),
                c_Coat('Мужское', 52),
                ]

res = 0 # Общий расход ткани
for clothe in Clothe_list:
    res += clothe.ClotheConsumption()
    print(clothe.Info)

print(f'Расход ткани требуемый для изготовления одежды: {round(res, 3)} м2')

'''
3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****.
'''
class c_Cell:
    NumberOfCell = 0

    def __init__(self, val):
        self.NumberOfCell = int(val)

    def __str__(self):
        return f'class c_Cell: NumberOfCell = {self.NumberOfCell}'

    def __int__(self):
        return self.NumberOfCell

    def __add__(self, other):
        res_cell = int(self) + int(other)
        return c_Cell(res_cell)

    def __sub__(self, other):
        res_cell = int(self) - int(other)
        if res_cell < 0:
            raise ValueError
        return c_Cell(res_cell)

    def __mul__(self, other):
        res_cell = int(self) * int(other)
        return c_Cell(res_cell)

    def __truediv__(self, other):
        res_cell = int(self) / int(other)
        return c_Cell(res_cell)

    def make_order(self, num_Cells_in_row):
        res = f'--- c_Cell.make_order({num_Cells_in_row}) ---\n'
        lst = [ '*' if i%num_Cells_in_row != 0 else '*\n'  for i in range(1, 1+self.NumberOfCell) ]
        # for i in range(1, 1+self.NumberOfCell ):
        #     res += '*'
        #     if i%num_Cells_in_row is 0:
        #         res+='\n'
        res += ''.join(lst)
        res += f'\n--END c_Cell.make_order({num_Cells_in_row})--\n'
        return res


print('=============================')
obj = c_Cell(16)
obj_1 = c_Cell(8)
print(obj.make_order(10))
print(obj.make_order(5))
print( f' {obj} + {obj_1} = {obj + obj_1}')
print( f' {obj} * {obj_1} = {obj * obj_1}')
print( f' {obj} / {obj_1} = {obj / obj_1}')
print( f' {obj} - {obj_1} = {obj - obj_1}')

