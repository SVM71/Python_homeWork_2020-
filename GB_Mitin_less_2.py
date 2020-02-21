'''
Урок второй - Практическое задание
'''
'''
1) Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию ​type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''
list_of_some = ['brakadabra', 5, True, 56.345, b'juyegjehfgwj']
for el in list_of_some:
    print(f'type: {type(el)}, val: {el}')

'''
2) Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию ​input().
'''
import ast

def tryeval(val):
  try:
    val = ast.literal_eval(val)
  except ValueError:
    pass
  return val

#user_inp = input("Please input list of any values digits or strings for example '1, 2,aa3':")
user_inp = '1,2, 3.4, True , hsgdshgd'

input_list = list( user_inp.replace(' ', '').split(',') )
#Lexical cast from string to type
#input_list = [tryeval(el) for el in input_list]

result = []
print('Начальный список :\n', input_list)
for i in range(len(input_list)//2):
    result.append(input_list[2*i+1])
    result.append(input_list[2*i])
if len(input_list)%2:
    result.append(input_list[len(input_list)-1])
print('Выполнен обмен значений соседних элементов:\n', result)

'''
3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
'''
month_season_data = [
    { 'month':'december',   'season':'winter' },
    { 'month':'january',    'season':'winter' },
    { 'month':'february',   'season':'winter' },
    { 'month':'march',      'season':'spring' },
    { 'month':'april',      'season':'spring' },
    { 'month': 'may',       'season':'spring' },
    { 'month':'june',       'season':'summer' },
    { 'month':'july',       'season':'summer' },
    { 'month':'august',     'season':'summer' },
    { 'month':'september',  'season':'autumn' },
    { 'month':'october',    'season':'autumn' },
    { 'month':'november',   'season':'autumn' },
]

while True:
    #user_inp = int(input("Please input the month number 1...12 :")
    user_inp = 12
    if user_inp is 0 or user_inp > 12:
        print('ERROR: wrong number!')
    else:
        break
indx = user_inp%12

print(  f'You input number: {user_inp}, month: { month_season_data[indx].get("month") }',
        f'season: { month_season_data[indx].get("season") }')

###############################################################
month_data = [ 'december', 'january', 'february',
               'march', 'april', 'may',
               'june', 'july', 'august',
               'september', 'october', 'november' ]
season_data = ['winter', 'spring', 'summer', 'autumn' ]

print(  f'You input number: {user_inp}, month: { month_data[indx] }',
        f'season: { season_data[indx&3] }')



'''
4) Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
только первые 10 букв в слове.
'''
# user_str = input("Пожалуйста вводите строку из нескольких слов, разделённых пробелами:")
user_str = 'FasFFdasd aDFDFfs adfdasfsdfsdfsdfsdfsdfsdfsdf ddTTdd HHdddd fff'

input_list = list( user_str.split(' '))
result_list = [ el if len(el) <= 10 else el[:10]  for el in input_list ]

print(f'\nСтрока пользователя: {user_str}')
print('''
Выводим  каждое слово с новой строки. Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове.''')
for el in enumerate(result_list):
    print(el)

'''
5) Реализовать структуру ​« ​Рейтинг ​» ​, представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, ​3 ​, 2.
Пользователь ввел число 8. Результат: ​8 ​, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, ​1 ​.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''
def append_num_2_list( list, num):
    list.append(num)
    list.sort(reverse = True)
    return list

''' 
посмотрел семинар... есть требование против reverse... 
'''
def append_num_2_list_v2( list, num):
    # предполагаем, список отсортирован по убыванию !!!
    # если не так то код не работает!!!
    indx = None
    for el in list:
        if num > el:
            indx = list.index(el)
            break

    if indx is None:
        list.insert(len(list), num)
    else:
        list.insert(indx, num)
    return list



my_list = [7, 5, 3, 3, 2]
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, ​3 ​, 2.
append_num_2_list( my_list, 3)
print(my_list)
#Пользователь ввел число 8. Результат: ​8 ​, 7, 5, 3, 3, 2.
append_num_2_list( my_list, 8)
print(my_list)
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, ​1 ​.
append_num_2_list( my_list, 1)
print(my_list)

my_list = [7, 5, 3, 3, 2]
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, ​3 ​, 2.
append_num_2_list_v2( my_list, 3)
print(my_list)
#Пользователь ввел число 8. Результат: ​8 ​, 7, 5, 3, 3, 2.
append_num_2_list_v2( my_list, 8)
print(my_list)
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, ​1 ​.
append_num_2_list_v2( my_list, 1)
print(my_list)




'''
6) *Реализовать структуру данных ​« ​Товары ​» ​. Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента ​— номер товара и словарь с параметрами (характеристиками товара: название,
цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
] Н
еобходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ ​—
характеристика товара, например название, а значение ​— список значений-характеристик,
например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}

'''
list_of_goods = [ (1, {'название': 'компьютер', 'цена': 20000,  'количество': 5, 'eд': 'шт.'}),
                  (2, {'название': 'принтер',   'цена': 6000,   'количество': 2, 'eд': 'шт.'}),
                  (3, {'название': 'сканер',    'цена': 2000,   'количество': 7, 'eд': 'шт.'})
                ]

def append_2_list_of_goods(dict):
    # при добавлении позиции если название цена и  ед совпадают то выполняем сложение поля цена
    for indx in range(len(list_of_goods)):
        l_dict = list_of_goods[indx][1]
        if l_dict.get('название') == dict.get('название')\
                and l_dict.get('цена') == dict.get('цена')\
                and l_dict.get('eд') == dict.get('eд'):
            list_of_goods[indx][1]['количество'] += dict.get('количество')
            return
    # иначе добавляем новую позицию...
    list_of_goods.append( (1+len(list_of_goods), dict) )

def get_analitics_list_of_goods():
    resilt_dict = {}
    for key in list_of_goods[0][1].keys():
        resilt_dict[key] = []
        for indx in range(len(list_of_goods)):
            resilt_dict[key].append(list_of_goods[indx][1].get(key))
    return resilt_dict


def form_data_4_list_of_goods():
    #Озадачиваем пользователя вопросами и заполняем поля словаря...
    #ЛИБО...
    return dict({'название': 'компьютер', 'цена': 20000,  'количество': 10, 'eд': 'шт.'})


###################################################
# добавляем в список...
append_2_list_of_goods(form_data_4_list_of_goods()) #такое имеется ...
# новая позиция
append_2_list_of_goods(dict({'название': 'суперкомпьютер', 'цена': 500700,  'количество': 3, 'eд': 'шт.'}))
# Выводим аналитику...
resilt_dict = get_analitics_list_of_goods()
for el in enumerate(resilt_dict.items()):
    print(el)