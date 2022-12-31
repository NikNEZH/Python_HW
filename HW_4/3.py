# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


from collections import Counter

my_list = [1,2,2,2,3,4,5,5,6,7,8,8]
counter = Counter(my_list)
a = []
for key, value in counter.items():
        if value <2:
            a.append(key)
print(a)