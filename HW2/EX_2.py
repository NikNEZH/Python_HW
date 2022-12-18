# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Enter number"))
my_List = []

def multiplikator(n):
    if n == 1:
        return 1
    else:
        return n * multiplikator(n - 1)

for i in range(1, n+1):
    if i == 1:
        my_List.append(1)
    else:
        my_List.append(multiplikator(i))

print(my_List)