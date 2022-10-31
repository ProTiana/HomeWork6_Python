# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Старый код
import random
# list = []
# for i in range(10):
#     list.append(random.randint(1, 10))
# print(list)
#
# result = []
#
# count = 0
# for i in list:
#     if list.count(i) == 1:
#         result.append(i)
# print(result)
# Новый вариант

list = [random.randrange(20) for i in range(10)]
print(list)
# list2 = [set(list)]
# print(list2)

# или
list2 = [i for n, i in enumerate(list) if i not in list[:n]]
print(list2)

#
# exp = lambda n:n*n
# print (exp(n))
# list = [i for i in range(1, n+1)]
# print (list)



