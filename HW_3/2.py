# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a = [2, 3, 5, 6]
lensd = len(a)
asd = []
c = 0
for i in range(0,lensd):
    if i < lensd/2:
        c = a[i-(i+i+1)] * a[i]
        asd.append(c)
    else:
        break
print(asd)

# Знаю немног костыльный код но лучше пока не придумал