'''
Практическое задание
1) Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import random
import string

def random_String(strlen=8):
    """Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits #+ string.punctuation
    result = ''.join( random.choice(letters) for i in range(strlen) ) + '\n'
    return result
#print( random_String() )

'''
1) Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''
def user_fill_file(file_name ):
    flag = True
    with open(file_name, 'w', encoding="utf-8") as f:
        while flag:
            user_inp = input('Введите строку символов для записи в файл, либо пустую строку для выхода:')
            if user_inp is '':
                print(f'Пустая строка, выход!')
                flag = False
            else:
                print(f'Пишем строку пользователя: \'{user_inp}\'')
                f.write(user_inp + '\n')

#user_fill_file('my_test_file.txt' )

'''
2) выполнит подсчет количества строк, и количества слов в каждой строке.
'''
def file_statistics( file_name ):
    result = { 'строк': 0, 'символов':0, 'символов в строке':[] }
    try:
        with open(file_name, 'r', encoding="utf-8") as f:
            for str in f:
                result['строк'] += 1
                result['символов'] += len(str)
                result['символов в строке'].append( len(str) )
    except IOError as err:
        print(err)
    finally:
        return result

#print ( file_statistics( 'my_test_file.txt' ) )

'''
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''
def low_income_stat(file_name):
    result = { 'сотрудники с окладом до 20тыс.': [], 'средний доход':0 }
    pers_cnt = 0
    try:
        with open(file_name, 'r', encoding="utf-8") as f:
            for str in f:
                pers_cnt += 1
                family, salary = str.split(' ')
                if float(salary) < 20000.0:
                    #print(str)
                    result['сотрудники с окладом до 20тыс.'].append(family)
                result['средний доход'] += float(salary)
    except IOError as err:
        print(err)
    finally:
        result['средний доход'] = round( result['средний доход']/ pers_cnt, 2 )
        return result

print ( low_income_stat( 'person_file.txt' ) )

'''
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
'''
dict_Conv_numeral = [
    {'en': 'one', 'ru': 'один'},
    {'en': 'two', 'ru': 'два'},
    {'en': 'three', 'ru': 'три'},
    {'en': 'four', 'ru': 'четыре'}
]

def user_translate_str(str):
    '''
    Перевод первого числительного с английского на русский
    строка: 'One xxxxx' будет заменена на  'Один  xxxxx'
    (если перевод не известен вернет строку без изменений.)
    :param str - строка для перевода:
    :return вернет строку:
    '''
    lst_str_words = str.split(' ')
    first_w = lst_str_words[0].lower()
    for el in dict_Conv_numeral:
        if el['en'] == first_w:
            lst_str_words[0] = el['ru'].title()

    result = ' '.join(lst_str_words)
    return result

def user_translate(fname):
    '''
    открывает файл fname на чтение и считывает построчно данные.
    При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
    Вернет название полученного файла с перевом в случае если все ОК
    '''
    try:
        outFname = fname.split('.')
        outFname[0] += '_tr.'
        str_outFname = ''.join(outFname)
        with open(fname, 'r', encoding='utf-8') as inpFile:
            with open(str_outFname, 'w', encoding='utf-8') as outFile:
                for str in inpFile:
                    outFile.write( user_translate_str(str) )
        return str_outFname

    except IOError as err:
        print(f'ERROR in user_translate(): {err}')
        return None

print(f"Получили файл '{ user_translate('one_two_free_for.txt')}' с переводом.")


'''
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
'''
import random

def user_genFile_wDigs():
    fname = 'File_wDigs.txt'

    with open(fname, 'w', encoding='utf-8') as oFile:
        res = []
        summ = 0
        for i in range(20):
            dig = random.randint(1, 1001)
            res.append(str(dig))
            summ += dig
        oFile.write(' '.join(res))
    return f'Записали в файл: \'{fname}\' список чисел:\n {res}\n Сумма чисел:{summ}'

print ( user_genFile_wDigs() )

'''
6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: 
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

def user_Predmet_stat(filename):
    result = {}
    try:
        with open(filename, 'r', encoding='utf-8') as i_File:
            for str in i_File:
                predmet = str.split(' ')[0][:-1]
                hours_lst = str.split(' ')[1:]
                dig_lst = [ int(s.split('(')[0]) for s in hours_lst if s.split('(')[0].isdigit() ]
                hours = sum(dig_lst)
                result[predmet] = hours
    except IOError as err:
        print(f'ERROR: Can\'t open file: \'{filename}\' ')
    return result

print( f' Result of call user_Predmet_stat("predmets_task6.txt"): {type(user_Predmet_stat("predmets_task6.txt"))}, '
       f'{user_Predmet_stat("predmets_task6.txt")}')

'''
7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''

def user_Firm_stat(filename):
    firms = {}
    result = [firms, {'average_profit': 0}]
    try:
        with open(filename, 'r', encoding='utf-8') as i_File:
            inp_data = i_File.readlines()
            firm_number = 0
            for str in inp_data[1:]:
                firm = str.split(' ')[0]
                profit = 0
                firm_number += 1
                lst_revenu_costs = str.split(' ')[2:]
                try:
                    profit = int(lst_revenu_costs[0])-int(lst_revenu_costs[1])
                except ValueError as err:
                    print(f'ERROR in file: \'{filename}\'! Can\'t convert to int: {lst_revenu_costs}')
                finally:
                    firms[firm] = profit
                    if profit >= 0:
                        result[1]['average_profit'] += profit

            result[1]['average_profit'] /= firm_number
            round(result[1]['average_profit'], 2)

    except IOError as err:
        print(f'ERROR: Can\'t open file: \'{filename}\' ')
    return result

import json
def user_save_Firm_stat(out_list, fileName):
    outFileName= fileName.split('.')[0] + '.json'
    with open(outFileName, 'w', encoding='utf-8') as o_File:
        json.dump(out_list, o_File)


res = user_Firm_stat("firm_data_task7.txt")
print( f' Result of call user_Firm_stat("firm_data_task7.txt"): {type(res)}, {res}')
user_save_Firm_stat(res, "firm_data_task7.txt")






