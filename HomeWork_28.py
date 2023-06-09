# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

# первый вариант
# def sum_(m, n):
#     return m if n == 0 else sum_(m + 1, n - 1) if n > 0 else sum_(m - 1, n + 1)   
# m, n = map(int, input().split()) # ввод через пробел
# print(sum_(m, n))

# второй вариант
def sum_(a, b):
    if not b:
        return a
    a += 1
    b -= 1
    return sum_(a, b)
a = int(input("введите число a: "))
b = int(input("введите число b: "))
print(sum_(a, b))