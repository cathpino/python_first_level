__author__ = 'Палуйыэ Екатерина Витальевна'

import math
import cmath
# easy
# Задача 1.1
print('Программа последовательного выведения знаков введнного числа.')
# Вариант с применением цикла while.
# Вариант задачи в normal лично для меня оказался проще, не получилось использовать арифметические действия.
# Так как в требованиях к заданию не было четко прописано оставить значения именно числом, уж больно велик соблазн
# использовать строку.
userNumber_1 = list(input('Введите, пожалуйста, число: '))
i = 0
while i < len(userNumber_1):
    print(userNumber_1[i])
    i += 1

# Вариант с применением цикла for.
userNumber_2 = list(input('Пожалуйста, введите еще одно число: '))
for f in userNumber_2:
    print(f)

# Задача 1.2
print('Программа изменения порядка вводимых переменных.')
firstVariable_A = int(input('Введите значение первой переменной A: '))
secondVariable_B = int(input('Введите значение второй переменной B: '))
supVariable_C = (secondVariable_B - firstVariable_A)  # Дополнительная переменная.

firstVariable_A += supVariable_C
secondVariable_B -= supVariable_C

print('A =', firstVariable_A, 'B =', secondVariable_B)

# Задача 1.3
print('Программа проверки доступа.')
userAge = int(input('Пожалуйста, укажте свой возраст: '))
normalAge = 18

if userAge >= normalAge:
    print('Доступ разрешен.')
if userAge < normalAge:
    print('Извините, пользование данным ресурсом только с 18 лет!')

# OR
userAge = int(input('Пожалуйста, подтвердите повторно свой возраст: '))

if userAge >= 18:
    print('Доступ разрешен.')
    access = True
else:
    print('Извините, пользование данным ресурсом только с 18 лет!')
    access = False

# normal
# Задача 2.1
print('Программа выведение наибольшей цифры из введенного числа.')
userNumber_3 = list(input('Введите произвольное целое число: '))
print(max(userNumber_3))

#OR
userNumber_6 = int(input('Введите еще одно произвольное целое число: '))
numeral = userNumber_6 % 10  # Делит левый операнд на правый и возвращает остаток. При делении на 10 таким образом
# от введенного числа будет отделена последняя цифра.
userNumber_6 = userNumber_6 // 10  # Деление в котором возвращается только целая часть результата. При делении на 10
# таким образом будут оставаться все цифры, за исключением последней.
while userNumber_6 > 0:
    if userNumber_6 % 10 > numeral:
        numeral = userNumber_6 % 10
    userNumber_6 = userNumber_6 // 10
print(numeral)

# Задача 2.2
# Пока пыталась разобраться с кортежем, решила сохранить попытки использования списков.
print('Программа по изменению порядка вводимых значений.')
lst = []
userNumber_4 = input('Введите значение первой переменной a: ')
userNumber_5 = input('Введите значение второй переменной b: ')
lst.append(userNumber_4)
lst.append(userNumber_5)
lst.reverse()
print(lst)

# OR
# Попытка использовать кортеж в Python.
userNumber_8 = input('Введите значение первой переменной x: ')
userNumber_9 = input('Введите значение второй переменной y: ')
x, y = (userNumber_8, userNumber_9)
x, y = y, x
print(x, y)

# Задача 2.3
# Здесь можно было бы обернуть в свою функцию def и использовать elif, но не хватило времени протестировать
# и разоброаться. Плюс округлить значению до нескольких знаков запятой.
print('Программа по вычислению корней квадратного уровнения.')
index_a = int(input('Введите значение коэффициента a: '))
index_b = int(input('Введите значение коэффициента b: '))
index_c = int(input('Введите значение коэффициента с: '))
d = index_b ** 2 - (4 * index_a * index_c)

if index_a == 0 and index_b == 0 and index_c != 0:
    print('Уравнение не имеет решений.')

if index_a == 0 and index_b == 0 and index_c == 0:
    print('Уравнение имеет бесчисленное множество решений.')

if index_a == 0 and index_b != 0 and index_c != 0:
    result = index_c / index_b
    print('Линейное уровнение, ответ:', result)

if d > 0 and index_a != 0:
    x_1 = (-index_b + math.sqrt(d)) / (2 * index_a)
    x_2 = (-index_b - math.sqrt(d)) / (2 * index_a)
    print('Корни уравнения:', x_1, x_2)

if d == 0 and index_a != 0 and index_b != 0 and index_c != 0:
    x_1 = (-index_b + math.sqrt(d)) / (2 * index_a)
    print('Действительные корни совпадают:', x_1)

if d < 0:
    x_1 = (-index_b - cmath.sqrt(d)) / (2 * index_a)
    x_2 = (-index_b + cmath.sqrt(d)) / (2 * index_a)
    print('Дискриминант отрицательный – корни комплексные:', x_1, x_2)

# hard
# Задание 3.1
# Результатом выполнения строчек ниже будет: True >> True >> True. Честно признаюсь, не поняла задание.
a = bool('0')
a == a**2
print(a)
a == a*2
print(a)
a > 999999
print(a)