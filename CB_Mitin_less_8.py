'''
Практическое задание
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
3) Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.

'''
#https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')
#print_format_table()

'''
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''
import re


class c_My_Date_RE:
    day = None
    month = None
    year = None

    def __init__(self, dt_dd_mm_yyyy):
        '''принимает дату в виде строки формата «день-месяц-год»'''
        try:
            m = re.search('\d\d-\d\d-\d{4}', dt_dd_mm_yyyy)
            c_My_Date_RE.day = [int(el) for el in m.group(0).split('-')][0]
            c_My_Date_RE.month = [int(el) for el in m.group(0).split('-')][1]
            c_My_Date_RE.year = [int(el) for el in m.group(0).split('-')][2]
        except AttributeError as err:
            print(f'ERROR DATE: {err}')

    @classmethod
    def get_date_as_numbers(cls):
        return c_My_Date_RE.day, c_My_Date_RE.month, c_My_Date_RE.year

    @staticmethod
    def is_valid_date():
        day_in_month = (31, 29 if c_My_Date_RE.year%4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        res = False
        if c_My_Date_RE.month in range(1, 13):
            if c_My_Date_RE.day in range(1, 1+day_in_month[c_My_Date_RE.month - 1]):
                if c_My_Date_RE.year > 0:
                    res = True
        return res


class c_My_Date:
    day = None
    month = None
    year = None

    def __init__(self, dt_dd_mm_yyyy):
        '''принимает дату в виде строки формата «день-месяц-год»'''
        try:
            c_My_Date.day = [int(el) for el in dt_dd_mm_yyyy.split('-')][0]
            c_My_Date.month = [int(el) for el in dt_dd_mm_yyyy.split('-')][1]
            c_My_Date.year = [int(el) for el in dt_dd_mm_yyyy.split('-')][2]
        except ValueError as err:
            print(f'ERROR DATE: {err}')

    @classmethod
    def get_date_as_numbers(cls):
        return c_My_Date.day, c_My_Date.month, c_My_Date.year

    @staticmethod
    def is_valid_date():
        day_in_month = (31, 29 if c_My_Date.year%4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        res = False
        if c_My_Date.month in range(1, 13):
            if c_My_Date.day in range(1, 1+day_in_month[c_My_Date.month - 1]):
                if c_My_Date.year > 0:
                    res = True
        return res

print('========= Without re lib ======')
#obj = c_My_Date('12-12-4s444')  #False
#obj = c_My_Date('13-13-4444')  #False
#obj = c_My_Date('29-02-2020')  #True
#obj = c_My_Date('29-02-2019')   #False
obj  = c_My_Date('29-02-2019')   #False
#obj  = c_My_Date('29-02-4444')   #True
print(c_My_Date.is_valid_date())
print(c_My_Date.get_date_as_numbers())
print('========= With re lib ======')
objRE  = c_My_Date_RE('29-02-2020')   #True
print(c_My_Date_RE.is_valid_date())
print(objRE.get_date_as_numbers())
print('============================')

'''
2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
'''
class c_User_ZeroDivisionError(ZeroDivisionError):
    def __init__(self, *args):
        super().__init__(args)
        self.ex = args

''' ТАК НЕ РАБОТАЕТ!!! Хотя казалось бы есть на кого возложить обработку.
try:
    1/0
except c_User_ZeroDivisionError as e:
    print('======> c_User_ZeroDivisionError', type(e), *e.ex)
    
    ТАК РАБОТАЕТ!!!
try:
    raise c_User_ZeroDivisionError('OOPS Zerodivision error occured!', 'Please, think before any action!')
except c_User_ZeroDivisionError as e:
    print('======> c_User_ZeroDivisionError', type(e), *e.ex)

    И ТАК РАБОТАЕТ!!!
try:
    raise c_User_ZeroDivisionError('OOPS Zerodivision error occured!', 'Please, think before any action!')
except ZeroDivisionError as e:
    print('======> ZeroDivisionError', type(e), *e.ex)
'''

while True:
    try:
        divide = 10#int(input('Введите число в числителе:'))
        divident = 1#int(input('Введите число в знаменателе:'))
        if divident is 0:
            raise c_User_ZeroDivisionError('Ошибка знаменатель не может быть равен 0!')
    except ValueError as err:
        print(f'Ошибка - {err}, некорректный ввод. Выход...' )
        break
    except c_User_ZeroDivisionError as err:
        print(*err.ex)
        continue
    else:
        print( f'Результат деления:  {divide}/{divident} = {divide/divident}' )
        break


'''
3) Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
'''
class c_User_IntConvError(Exception):
    def __init__(self, *args):
        super().__init__(args)
        self.ex = args

import ast
def tryeval(val):
  try:
    val = ast.literal_eval(val)
  except ValueError:
    pass
  return val

class c_User_Parser:
    INP_IS_DIGIT = 1
    INP_ERROR = 2
    INP_STOP = 3
    #result_list = None

    def __init__(self):
        self.result_list = []

    def result_list(self):
        return self.result_list

    def ParseInp(self, str):
        res = self.INP_IS_DIGIT
        try:
            val = tryeval(str.strip())
        except SyntaxError:
            raise c_User_IntConvError('ОШИБКА ВВОДА! Требуется ввести число...')
        else:
            #print(f'ParseInp(): user_input = {str}, type_val ={type(val)}, val ={val}')
            if type(val) == type(' '):
                if val.lower() == 'stop':
                    res = self.INP_STOP
            else:
                #if type(val) == type(1) or type(val) == type(1.0):
                self.result_list.append(val)
            return res
############################################
user_Parser = c_User_Parser()
while True:
    try:
        user_inp = 'stop'#input('Введите новое число, для заполнения списка. либо \'stop\' для завершения:').strip()
        print(f'ParseInp(): user_input = {user_inp}')
        if user_Parser.ParseInp(user_inp) == c_User_Parser.INP_STOP:
            break
    except c_User_IntConvError as err:
        print(*err.ex)

print(user_Parser.result_list)

'''
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''
import datetime
import time
import copy

class c_Store:

    def __init__(self, list_StoreItems=None, list_TransferItems=None):
        self.list_StoreItems = list_StoreItems if type(list_StoreItems) == type([]) else []
        self.list_TransferItems = list_TransferItems if type(list_TransferItems) == type([]) else []
        self.__Current_ID = len(self.list_StoreItems) + len(self.list_TransferItems)

    def addItems(self, item, quantity, supply_info):
        # if type(item) != type(c_StoreItem('')):
        #     raise TypeError(f'Type of item: {type(item)} must be c_StoreItem')
        for indx in range(quantity):
            item.Store_id = self.__Current_ID
            item.supply_info = supply_info
            item.acceptDate = datetime.datetime.now()
            self.list_StoreItems.append(copy.deepcopy(item))
            self.__Current_ID += 1

    def giveItem(self, Store_id, consumer_Info):
        store_ids = [item.Store_id for item in self.list_StoreItems]
        if Store_id not in store_ids:
            return ''
            #raise ValueError(f'Error! Not Find Item with Store_Id:{Store_id}')

        itm = self.list_StoreItems.pop( store_ids.index(Store_id) )
        itm.transferDate = datetime.datetime.now()
        itm.consumer_Info = consumer_Info
        self.list_TransferItems.append(itm)
        return itm.item.info

    # веренет спсиок c_OfficeEquipment
    def FindBy_SupplyInfo(self, supply_info):
        pass
    # веренет спсиок c_OfficeEquipment
    def FindBy_AcceptanceDate(self, acceptDate):
        pass
    def GetItems_InStore(self):
        return self.list_StoreItems
    def Get_TransferredItems(self):
        return self.list_TransferItems

    def __str__(self):
        res = f'Состояние склада, всего {len(self.list_StoreItems)} позиций:\n'
        for item in self.list_StoreItems:
            res += str(item)
        res += f'\nПередано со склада, всего {len(self.list_TransferItems)} позиций:\n'
        for item in self.list_TransferItems:
            res += str(item)
        return res


class c_StoreItem:
    __slots__ = ('item',
                 'Store_id',
                 'acceptDate',
                 'transferDate',
                 'supply_info',
                 'consumer_Info'
                )

    def __init__(self, item=None):
        self.item = item
        self.Store_id = None
        self.acceptDate = None
        self.transferDate = None
        self.supply_info = None
        self.consumer_Info = None

    def __str__(self):
        res = f' ID товара: {self.Store_id},' \
              f'\nдата приема:\t{self.acceptDate},\tпоставщик: {self.supply_info}' \
              f'\nдата передачи:\t{self.transferDate},\tпередано: {self.consumer_Info}'
        return res


class c_Printer(c_StoreItem):
    def __init__(self, prod_name, price, manuf_info = None):
        self.prod_name = prod_name
        self.price = price
        self.manuf_info = manuf_info
        self.category = 'Printer'
        super().__init__(self)

    @property
    def info(self):
        res = f'ITEM_INFO: category: {self.category}, prod_name: {self.prod_name}, price: {self.price}, manuf_info: {self.manuf_info}'
        return res

    def __str__(self):
        res = self.info
        res += f'\nstore_data: {super().__str__()}'
        return res

class c_Scanner(c_StoreItem):
    def __init__(self, prod_name, price, manuf_info = None):
        self.prod_name = prod_name
        self.price = price
        self.manuf_info = manuf_info
        self.category = 'Scanner'
        super().__init__(self)

    @property
    def info(self):
        res = f'ITEM_INFO: category: {self.category}, prod_name: {self.prod_name}, price: {self.price}, manuf_info: {self.manuf_info}'
        return res

    def __str__(self):
        res = self.info
        res += f'\nstore_data: {super().__str__()}'
        return res

class c_Xerox(c_StoreItem):
    pass
    def __init__(self, prod_name, price, manuf_info = None):
        self.prod_name = prod_name
        self.price = price
        self.manuf_info = manuf_info
        self.category = 'Xerox'
        super().__init__(self)

    @property
    def info(self):
        res = f'ITEM_INFO: category: {self.category}, prod_name: {self.prod_name}, price: {self.price}, manuf_info: {self.manuf_info}'
        return res

    def __str__(self):
        res = self.info
        res += f'\nstore_data: {super().__str__()}'
        return res

############################################################
store = c_Store()
obj1 = c_Printer('LaserJet', 1250.00, 'Hewlet Pakkard' )

store.addItems(obj1, 3, 'Ситилинк' )
print(f'======== НА СКЛАДЕ ========'
      f'\n{store}\n'
      f'==========================='
)
time.sleep(2)
item = store.giveItem(0, 'отдел БухУчет, пользователь Петров В.В' )
print(f'Передаем: {item}\n в отдел БухУчет, пользователь Петров В.В.')

print(f'======== НА СКЛАДЕ ========'
      f'\n{store}\n'
      f'==========================='
)

'''
7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
'''
class c_User_Complex:
    #TypeError: complex() second arg can't be a string
    def __init__(self, re, im):
        if type(re) == type(1) or type(re) == type(1.0):
            self.re = re
        else:
            raise TypeError('c_User_Complex() can\'t take second arg if first is a string')

        if type(im) == type(1) or type(im) == type(1.0):
            self.im = im
        else:
            raise TypeError('c_User_Complex() second arg can\'t be a string')

    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return c_User_Complex(re, im)

    def __mul__(self, other):
        ''' Произведением двух комплексных чисел z1=a1+b1i и z2=a2+b2iz2=a2+b2i называется комплексное число z, равное
         z = z1⋅z2 = (a1a2−b1b2)+(a1b2+b1a2)i '''

        re = (self.re*other.re - self.im*other.im)
        im = (self.re*other.im + other.re*self.im)
        return c_User_Complex(re, im)

    def __str__(self):
        return f"({self.re}{'+' if self.im >= 0 else ''}{self.im}j)"


c1 = complex(1.5,-11)
c2 = complex(3,-3.99)
u1 = c_User_Complex(1.5,-11)
u2 = c_User_Complex(3,-3.99)

print(f' MULTIPLY OP complex: {c1*c2}\tc_User_Complex: {u1*u2}' )
print(f' ADDITION OP complex: {c1+c2}\tc_User_Complex: {u1+u2}' )

