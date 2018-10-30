__author__ = 'Палуйыэ Екатерина Витальевна'

# Все задачи текущего блока решите с помощью генераторов списков!
# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

from random import randrange
from random import randint

n = 6
myList = [randrange(-100, 100) for i in range(n)]

modList2 = []
for i in myList:
    modList2.append(i ** 2)
print(modList2)

#OR

modList3 = myList[:]
modList3 = [i ** 2 for i in modList3]
print(modList3)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Как только сгенерировать список из слов? Если в задании сказано "Все задачи текущего блока решите с помощью генераторов".
listFruit1 = ['x', 'y', 'z', 'a']
listFruit2 = ['x', 'a']
commonFruit = list(set(listFruit1) and set(listFruit2))
print(commonFruit)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

myList4 = [randrange(-1000, 1000) for i in range(1000)]
myList5 = [i for i in myList4 if i % 3 == 0 and i % 4 != 0 and i >= 0]
print(myList5)


# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# Это то, что было в процессе понимания, как это должно работать.
#modList7 = []
#for c in line:
#    if c.islower():
#        modList7.append(c)
#print(modList7)

#lowercase_letters = ','.join([c for c in line if c.islower()])
#print(lowercase_letters)

#lowers = [c for c in line if c.islower()]
#print(lowers)


result = ''

for j in range(len(line)):
    if line[j] == line[j].lower():
        if line[j] == line[j-1] and line[j] != line[j+1]:
               line = line[:j+1] + ',' + line[j+1:]
        result += line[j]
print(result)

# Остальные задания пока не выполнены.
