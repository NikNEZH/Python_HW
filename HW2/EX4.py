# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите
# произведение элементов на указанных позициях. Позиции хранятся в отдельном
# списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].



# from math import prod
from random import randint
n = int(input("N"))
arr = [randint(-n, n) for x in range(1, n+1)]
print(arr)
print( arr[int(input("Введите позицию первого элемента"))] * arr[int(input("Введите позицию второго элемента"))])
# print(f'Произведение элементов списка: {prod(arr)}')

# Надеюсь я правильно понял задачу спрошу у вас на семинаре по поводу вот этих from random import randint
# не понимаю что это