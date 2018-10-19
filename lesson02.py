__author__ = 'Палуйыэ Екатерина Витальевна'

import math
from random import randrange
from random import randint
# easy
# Задача 1.1
# Вариант 1
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
fruits1 = fruits[:]
i = 1

for item in fruits:
    print(i, '{:>8}'.format(item), sep = '.')
    i += 1

# Вариант 2
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
i = 1

for item in range(len(fruits)):
    print(i, '%8s' % fruits[item], sep = '.')
    i += 1

# Задача 1.2
a = (list(range(10)))
b = [randint(0, 15) for i in range(10)]
print(a)
print(b)
A = set(a)
B = set(b)
A -= B
a = list(A)
print(a)

# Задача 1.3
n = 6
a = [randrange(1, 20000) for i in range(n)]
print(a)
b = [i / 4 for i in a if i % 2 == 0] + [i * 2 for i in a if i % 2 != 0]
print(b)
print(a)

# normal
# Задача 2.1
# Задача 2.2
# Не выполнено

# Задача 2.3
v = [randint(-100, 100) for i in range(55)]
print(v)

# Задача 2.4
lst = [1, 2, 4, 5, 6, 2, 5, 2]
C = set(lst)
D = [i for i in lst if lst.count(i) == 1]
print(C)
print(D)

# Дополнительное задание (не до конца)
p = [randint(0, 15) for i in range(10)]
print(p)
a = p[1::2] #здесь запуталась, места = индексы, тогда будет a = p[::2]
print(a)
s = sum(a)
print(s)

day = {"31": "тридцать первое", "01": "первое", "02": "второе", "03": "третье"}
sortDay = sorted(day.items(), key=lambda value: value[1])
print(sortDay)
