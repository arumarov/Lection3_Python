# ФАЙЛЫ
# Как работать с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+, r+

# # Один из способов записи данных в файл:
# colors = ['red', 'green', 'blue123'] # список
# data = open('file.txt', 'a') # создаем текстовую переменную и связываем ее с текстовым файлом (указываем путь и мод)
# # если указан мод 'a', при каждом запуске в файл file.txt будет дозаписываться 'redgreenblue'
# # data = open('file.txt', 'w') # при данном моде информация в файл будет перезаписываться
# # data.writelines(colors) # функционал, позволяющий записать некоторый набор данных, разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 13\n')
# data.close() # закрытие файла

# # Еще способ записи данных в файл:
# with open('file.txt', 'w') as data: # (указываем что то, что в скобках должно восприниматься как data)
#     data.write('line 111\n')
#     data.write('line 222\n')
# # в данном режиме не нужно в ручном режиме вызывать закрытие файла, он закроется автоматически

# # Способ чтения данных из файла
# path = 'file.txt' # создаем путь к файлу
# data = open(path, 'r') # открываем файл в режиме чтения
# for line in data:  # в режиме цикла проходим по файлу
#     print(line) # считываем все строки, данный оператор делает переход на новую строку
# data.close() # разрываем связь с файлом


# ФУНКЦИИ И МОДУЛИ

# Обращаемся к функции из другого файла
# import lection1 # указываем имя файла, к которому обращаемся
# print(lection1.f(1)) # указываем имя файла и наименование функции, которую вызываем

# import lection1 as l1 # то же, что и в предыдущем примере, но присваиваем lection1 имя l1
# print (l1.f(1))

# Значения по умолчанию для функции
# def new_string(symbol, count): # функция принимает некоторый символ и некоторое число
#     return symbol * count # в python можно умножать строку на число
# print(new_string('!', 5))   # результатом будет !!!!!
# print(new_string('!'))      # указан только один аргумент, соответственно вызов будет с ошибкой

# def new_string(symbol, count = 3): ## указываем, что count по умолчанию будет равен 3
#     # значений по умолчанию может быть сколько угодно, но описываются они самыми последними
#     return symbol * count
# print(new_string('!', 5))   # ответ - !!!!!
# print(new_string('!'))      # ответ - !!! (так как второй аргументявно  не указан)
# print(new_string(4))        # 12 (так как второй аргумент явно не указан)

# Возможность передачи неограниченного количества элементов
# def concatenatio(*params): # при описании ставим * перед аргументом
#     res: str = "" # явно прописываем тип данных
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))  # вывод - asdw
# print(concatenatio('a', '1'))  # вывод - a1
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# Рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# КОРТЕЖИ
# # a, b = 3, 4 # множественное присваивание, a = 3, b = 5
# a = (3, 4, 41, 23) # создание кортежа
# b = (3,) # создание кортежа из одного элемента
# print(a)
# print(a[0]) # вызов конкретного элемента кортежа
# print(a[-2]) # вызов конкретного элемента кортежа
# # нельзя как в списках присвоить 

# t = ()
# print(type(t))   # tuple
# t = (1,)
# print(type(t))   # tuple
# t = (1)
# print(type(t))   # int
# t = (28, 9, 1990)
# print(type(t))   # tuple
# colors = ['red', 'green', 'blue']
# print(colors)    # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)         # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue']) # создание кортежа их списка
# print(t[0])      # red
# print(t[2])      # blue
# # print(t[10])   # IndexError: tuple index out of range
# print(t[-2])     # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t: # перебор кортежа при помощи цикла
#     print(e)     # red green blue
# t[0] = 'black'   # TypeError: 'tuple' object does not support item assignment

# a = (3, 4, 5)
# print(a)
# print(a[0])
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue']) # создаем список, конвертируем его в кортеж
# red, green, blue = t # распаковываем и превращаем его в 3 независимые переменные
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue


# СЛОВАРИ
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# # типы ключей могут отличаться
# print(dictionary['up'])   # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left'])  # ⇐
# #print(dictionary['type'])  # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# for k in dictionary.keys(): # вывести ключи словаря
#     print(k)

# for k in dictionary.values(): # вывести значения словаря
#     print(k)

# for v in dictionary: # вывести словарь
#     print(v)

# for v in dictionary: # вывести словарь (только значения)
#     print(dictionary[v])


# МНОЖЕСТВА
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a))  # set
# print(type(b))  # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a))  # set
# print(type(b))  # set
# print(type(c))  # set
# a = {1, 1, 1, 1, 1}
# print(a)  # {1}

# colors = {'red', 'green', 'blue'}
# print(colors)   # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)   # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)   # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors)   # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red')  # ok
# print(colors)   # {'green', 'blue','gray'}
# colors.clear()   # { }
# print(colors)   # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()  # c = {1, 2, 3, 5, 8} # копирование множества
# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21} # объединение множеств
# i = a.intersection(b)  # i = {8, 2, 5} # пересечение множеств
# dl = a.difference(b)  # dl = {1, 3} # установление разницы двух множеств (a - b)
# dr = b.difference(a)  # dr = {13, 21} # установление разницы двух множеств (b - a)
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a) # создание неизменяемого(замороженного) множества
# print(b) # frozenset({1, 2, 3, 5, 8})

# СПИСКИ
# list1 = [1,2,3,4,5]
# list2 = list1 # копирование списка

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123 # меняем значение в list1, значение в скопированном list2 также меняется
# list2[1] = 333 # меняем значение в list2, значение в list1 также меняется

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1 = [1,2,3,4,5]
# print(len(list1))
# print(list1.pop()) # удаление последнего элемента
# print(list1)
# print(list1.pop()) 
# print(list1)
# print(list1.pop()) 
# print(list1)

# list1 = [1,2,3,4,5]

# print(list1.pop(2)) # удаление элемента с индексом 2
# print(list1)

# print(list1.insert(2, 11)) # добавление в список элемента 11 (после элемента с №2)
# print(list1)

# print(list1.append(11)) # добавление элемента в конец списка
# print(list1)