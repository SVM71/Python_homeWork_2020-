'''
Практическое задание
'''
'''1) Реализовать функцию, принимающую два числа (позиционные аргументы) 
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def division_func(nom, denom):
    '''
    функция, принимает два числа (позиционные аргументы), и выполняет деление.
    вернет результат деления, либо строку - соообщение об ошибке...
    :param nom: делимое
    :param denom: делитель
    :return:
    '''
    try:
        return nom/denom
    except ZeroDivisionError:
        return 'OOPS zero division error!!!'

nom = 5#float(input('Введите делимое, целое или вещественное:'))
denom = 1#float(input('Введите делитель, целое или вещественное:'))
print(f'результат деления: {division_func(nom, denom)}')

'''2) Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
'''
def User_data_info(**kwargs):
    res= str(kwargs)
    return res

res = User_data_info( name='Вася', surname='Пупкин',\
                      birthday='20.01.2000', town='Moscow',\
                      email='vasya_2000@gmail.com', phone='84953334256')
print(f'type: {type(res)}\nvalue: {res}')

'''3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
'''
def get_summ_og_biggest(*args):
    r= list(args)
    r.sort(reverse=True)
    return sum(r[:2])


print( f'get_summ_og_biggest(31,5,9) = {get_summ_og_biggest(31, 5, 9)}')

'''4) Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
    Первый — возведение в степень с помощью оператора **. 
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
def my_power_v1(base, degree):
    return int(base) ** int(degree)

def my_power_v2(base, degree):
    res = base
    for i in range(1, int(degree)):
        res = res * base
    return res

print(f' my_power_v1(base, degree):2 в степени 5 = {my_power_v1(2,5)}')
print(f' my_power_v2(base, degree):2 в степени 5 = {my_power_v2(2,5)}')

'''5) Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить 
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
user_sum = 0
flag = True
while flag:
    user_inp = input('Введите строку чисел разделенных пробелом, либо символ \'x\' или \'X\':')
    user_inp_list = user_inp.split(' ')
    user_dig_list = []
    for el in user_inp_list:
        try:
            val = int(el)
            user_sum += val
            user_dig_list.append(val)
        except ValueError:
            print(f'ОШИБКА некорректный ввод: {el}')
            if el.find('x') != -1 or el.find('X') != -1:
                print(f' Найден символ для выхода \'x\' или \'X\': {el}')
                flag = False
            else:
                pass

    print(F'Пользователь ввел список чисел:{user_dig_list}\n Сумма цифр с учетом предыдущей суммы: {user_sum}' )

'''6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
'''
def Chng_str(user_str):
    #return user_str.capitalize()
    res = user_str[0].upper() + user_str[1:]
    return res

#test Chng_str
#print(Chng_str('cccc'))
#print(Chng_str('SccC'))

user_str = 'asdad asdasd adsasd adssad asdas AAAasdsa sdsfsdAAA'
user_str_list = user_str.split(' ')
result = ''
for s in user_str_list:
    result += Chng_str(s) + ' '

print('Исходная строка:\t', user_str)
print('Cтрока результат:\t', result)

