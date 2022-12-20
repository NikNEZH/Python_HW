# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
my_list = [1.1, 1.2, 3.1, 5, 10.01]

def max(a):
    x = 0.001
    for i in a:
        b = float(i)
        y = b - math.floor(b)
        if y > x:
            x = y
    return x
def min(a):
    c = 0.9
    for i in a:
        x = float(i)
        y = x - math.floor(x)
        if y < c:
            c = y
    return c

minimum = min(my_list)
maximum = max(my_list)
result = maximum - minimum

print(result)
