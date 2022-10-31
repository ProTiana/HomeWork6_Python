# 2
# #Напишите программу, которая найдёт произведение пар чисел списка.
# #Парой считаем первый и последний элемент, второй и предпоследний
# Старый код
# lst = [1,2,4,5,5,3,7,8,9]
# product = 0
# for i in range(len(lst)):
#     if i < (len(lst)/2):
#        product = lst[i]*lst[len(lst)-1-i]
#        print(product)
# Новый вариант
lst = [1,2,4,5,5,3,7,8,9]
product = lambda x, y: x*y
lst1 = [product(lst[i], lst[len(lst)-1-i]) for i in range(len (lst)) if i<(len(lst)/2)]
print(lst1)