# 3
# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55
# Старый код
# n = int(input("Введите значение: "))
# result =0
# for i in range (1, n+1):
#     result += (1+(1/i))**i
# print(result)
# Новый вариант
n = int(input("Введите значение: "))
result = [(1+(1/i))**i for i in range(1, n+1)]
sum=0
for i in range(len(result)):
    sum += result[i]
print(sum)