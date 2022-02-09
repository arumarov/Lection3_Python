# ТИПЫ ДАННЫХ И ПЕРЕМЕННЫЕ
# int, float, boolean, str, list, None
# value = None
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# value = 12334
# # print(type(value))
# s = 'hello world'

# # print(s)
# # print(a, b, s)
# print(a, '-' ,b, '-' ,s) # вариант вывода переменных
# print('{} - {} - {}'.format(a, b, s)) # вариант вывода переменных
# print(f'{a} - {b} - {s}')# вариант вывода переменных
# print('{1} - {2} - {0}'.format(a, b, s)) # вариант вывода переменных, с заменой порядка вывода

# f = False
# print(f)

# СПИСКИ
# list = [1,2,3]
# list = ['1','2','3', 'hello', 1, 2, 4.5, True] # можно, но не нужно помещать в один список данные одного типа
# list = ['1','2','3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)

# ВВОД И ВЫВОД ДАННЫХ
# print('введите a')
# a = float(input())
# print('введите b')
# b = float(input())
# print(a, b)
# print(a, ' + ', b, ' = ', a+b)

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
# a = 1.31233
# b = 3
# c = a // b # деление до целого
# c = a % b # остаток от деления
# c = a ** b # возведение в степень
# c = round(a * b, 5) # округление по математическим правилам, указывается до скольки знаков требуется округление
# print(c)

#присваивание
# a = 3
# a += 5 # аналогично выражению a = a + 5
# print(a)


# ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 > 4 and 5 > 2
# a = 1 == 2 # операция сравнения
# a = 1 != 2 # операция неравенства
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b) # сравнение строк

# a = [1, 2]
# b = [1, 2]
# print(a == b) # сравнение списков

# a = 1 < 3 < 5 <10 # можно указывать не только двойные неравенства
# print(a)
# func = 1
# T = 4
# x = 123
# print(func<T>x)

# f = 1 > 2 or 4 < 6
# f = [1, 2, 3, 4]
# print(f)
# # print(2 in f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0 # обращаемся к первому числу списка f, проверяем на четность
# is_odd = not f[0] % 2 # так как считается, что 0 - false, 1 - true, можно представить выражение таким образом
# print(is_odd)

# Управляющие конструкции: if, if-else (отступы важны!)
# if condition: # указываем условие
#     # operator 1 # набор операторов
#     # operator 2
#     # ...
#     # operator n
# else:
#     # operator n + 1 # набор операторов
#     # operator n + 2
#     # ...
#     # operator n + m

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# if condition1:
#     # operator
# elif condition2: # если не выполняется if, проверяется следующее условие
#     # operator
# elif condition3:
#     # operator
# else:
#     # operator

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет,', username)

# Управляющие конструкции: while (отступы важны!)
# while condition: # указываем условие
#     # operator 1 # набор операторов
#     # operator 2
#     # ...
#     # operator n

# original = 23
# inverted = 0
# while original != 0: # пока original не равен нулю
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# while condition: # указываем условие
#     # operator 1 # набор операторов
#     # operator 2
#     # ...
#     # operator n
# else: # указываем условие
#     # operator 1 + n # набор операторов
#     # operator 2 + n
#     # ...
#     # operator n + m

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)


# Управляющие конструкции: for
# for i in enumeration: # переменная i, которая будет являться счетчиком, затем in, затем итерируемый объект(например список)
#     # operator 1
#     # operator 2
#     # ...
#     # operator n

# for i in 1, -2, 3, 14, 5:
#     print(i**2) #выводим квадрат i

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
# for i in range(1, 5): # можно сразу записать range в условие
# for i in range(1, 10, 2): # третий аргумент - приращение на 2
#     print(i)

# for i in 'qwerty':
#     print(i)


# Немного о строках
# text = 'съешь ещё этих мягких французских булок'

# print(len(text)) # показывает количество символов
# print('ещё' in text) # проверяет наличие строки в подстроке
# print(text.isdigit()) # проверяет, являются ли все символы строки числами
# print(text.islower()) # проверяет, являются ли все символы строки символами нижнего регистра
# print(text.replace('ещё', 'ЕЩЁ'))

# for c in text:
#     print(c)

# help(text.isdigit) # вызывает помощь по команде

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])   # c - обращаемся к конкретному элементу строки по его индексу
# print(text[1])   # ъ - обращаемся к конкретному элементу строки по его индексу
# print(text[len(text)-1])  # к - если просто ввести len(text) будет ошибка, т.к. индексация с 0, поэтому вычитаем 1
# print(text[-5])  # б - обращаемся к конкретному элементу строки по его индексу (со знаком минус - отсчет идет от конца строки)
# print(text[:])   # print(text) - по умолчанию проставляются первый и последний аргумент, выводится вся строка
# print(text[:2])  # съ - по умолчанию в начале проставляется первый(нулевой) символ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...


#Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]

# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# print(f'{len(numbers)} len')  # [10, 2, 3, 4, 5]

# for i in numbers:
#     i *= 2      # - не записывает данные в список
#     print(i)    # [20, 4, 6, 8, 10] 
# print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)   # red green blue
# for e in colors:
#     print(e*2)   # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции
# def function_name(x): # def имя_функции(аргументы)
# # body line 1 # тело метода
# # . . .
# # body line n
#     # optional return 

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 1
# print(f(arg))
# print(type(f(arg)))