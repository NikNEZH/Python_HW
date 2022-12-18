# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
n = int(input("Enter n"))
a = []
for i in range(1, n+1):
    c = round((1+1/i) ** i, 3)
    a.append(c)
print(a)