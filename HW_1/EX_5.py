# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def cordiant(x):
    xy = ["X", "Y"]
    my_List = []
    for i in range(x):
        flag = False
        while not flag:
            try:
                number = int(input(f"Введите число для {xy[i]}: "))
                my_List.append(number)
                flag = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return my_List


def calculate(a, b):
    segment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return segment

print("Введите координаты точки А")
pointA = cordiant(2)
print("Введите координаты точки В")
pointB = cordiant(2)

print(f"Длина отрезка: {format(calculate(pointA, pointB), '.2f')}")