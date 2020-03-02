
from sys import argv
from GB_Mitin_less_4 import Calk_Salary

#print(f' type of argv: {type(argv)}, len(argv): {len(argv)}, argv_data: {argv} ')

if len(argv) > 3 and  len(argv) < 5:
    hours = float(argv[1])
    payload = float(argv[2])
    premium = 0
    if len(argv) == 4:
        premium = float(argv[3])
    print(f' Зарплата составит: {Calk_Salary(hours, payload, premium)} тугриков')
else:
    print('Ошибка! Мало параметров. Требуется передать колич_часов, ставка, премия в % от отработанного.\n'
          'Пример запуска: python GB_Mitin_less_4_script.py 4 1000 20')