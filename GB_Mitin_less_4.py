'''
Практическое задание

1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

2) Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.

4) Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования
в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]

5) Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

6) Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

7) Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

'''
1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия в процентах от отработанного.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
def Calk_Salary(work_time, pay_per_hour, premium_pers = 0):
    return  work_time*pay_per_hour + round( work_time*pay_per_hour*premium_pers/100, 2)

if __name__ == '__main__':
    '''
    2) Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
    Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
    Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
    Результат: [12, 44, 4, 10, 78, 123].
    '''
    input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [ input_list[indx] for indx in range(1, len(input_list)) if input_list[indx] > input_list[indx-1]]
    print(result)

    '''
    3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
    Подсказка: использовать функцию range() и генератор.
    '''
    result = [el for el in range(20, 241) if el % 20 is 0 or el % 21 is 0 ]
    print(result)

    '''
    4) Представлен список чисел. Определить элементы списка, не имеющие повторений.
    Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования
    в исходном списке. Для выполнения задания обязательно использовать генератор.
    Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
    Результат: [23, 1, 3, 10, 4, 11]
    '''
    input_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [input_list[indx] for indx in range(len(input_list)) if input_list.count(input_list[indx]) == 1]
    print(result)

    '''
    5) Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
    результат вычисления произведения всех элементов списка.
    Подсказка: использовать функцию reduce().
    '''
    from functools import reduce

    def my_func(prev_el, el):
        # prev_el - предыдущий элемент
        # el - текущий элемент
        return prev_el * el

    input_list = [dig for dig in range(100, 1001)]
    #input_list = [dig for dig in range(8, 11)]
    print( f'Результат вычисления произведения всех элементов списка:\n{input_list}'
           f' \nresult: {reduce(my_func, input_list)}' )
    print( f'Результат вычисления произведения всех элементов списка result_reduce_lambda:'
           f' \nresult: {reduce(lambda x, y: x*y, input_list)}' )

    '''
    6) Реализовать два небольших скрипта:
        а) итератор, генерирующий целые числа, начиная с указанного,
        б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
    не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
    Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
    Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
    '''
    import itertools, random

    #а) итератор, генерирующий целые числа, начиная с указанного,
    def my_int_iter(start, stop):
        res = (el for el in range(start, stop+1))
        return res

    #б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    def my_lst_iter(i_list):
        res = (el for el in i_list)
        return res


    start = 3
    end = 6
    for el in itertools.cycle(my_int_iter(start,end)):
        print(el)
        if el == end:
            break

    inp_list = [random.randint(0,100) for i in range(4)]
    for el in itertools.cycle(inp_list):
        print(el)
        if el == inp_list[len(inp_list)-1]:
            break

    '''
    7) Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
    При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
    for el in fact(n) !!!!-- Смешение понятия итератор и функция вычисления факториала!!!!
    . Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
    начиная с 1! и до n!.
    Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
    '''
    def fact_fun(numb):
        return reduce(my_func, [el for el in range(1, numb+1)] )

    def fact_iter(numb):
        #yield [ el for el in range(1, numb+1) ] # так вернет список [ 1, ... numb]
        yield ( el for el in range(1, numb+1) ) # так вернет итератор  ( 1, ... numb )

    num = 4
    print('==========================')
    for dig in fact_iter(num):
        print(dig, fact_iter(num))
        for el in dig:
            print(f' factorial of {el} is {fact_fun(el)}')
    print('==========================\n')
