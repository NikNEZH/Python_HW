# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).
def getQuarterNumbers (x, y):
    a = []
    for i in range(x, y):
        a.append(i)
    return a
def checkCoordinates(quarter):
    if quarter == 1:
        print(f"диапазон координат точек в этой четверти {getQuarterNumbers (1, 10)} четверти плоскости")
    elif quarter == 2:
        print(f"диапазон координат точек в этой четверти {getQuarterNumbers (-10, 10)} четверти плоскости")
    elif quarter == 3:
        print(f"диапазон координат точек в этой четверти {getQuarterNumbers (-1, -10)} четверти плоскости")
    elif quarter == 4:
        print(f"диапазон координат точек в этой четверти {getQuarterNumbers (10, -10)} четверти плоскости")
    else:
        print(f"Всего 4 четверти пожалуйста введите коректные данные ")


numbers = int(input("Введите число для четверти"))
checkCoordinates(numbers)