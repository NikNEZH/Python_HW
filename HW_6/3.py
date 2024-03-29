# 1) Больше предыдущего
#
# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа,
# то есть, стоят вслед за меньшим числом.
#
# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.
#
# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.
#
# Тестовые данные
# Sample Input 1:
# 1 2 3 4 5
# Sample Output 1:
# 4
# Sample Input 2:
# 1 1 3 2 2 1 1 1 1
# Sample Output 2:
# 1
# Sample Input 3:
# 5 4 3 2 1
# Sample Output 3:
# 0

enteredNumber = "1 1 3 2 2 1 1 1 1"
listOfNumbers = enteredNumber.split()
count = 0
#
# for i in range(len(listOfNumbers) - 1):
#     if listOfNumbers[i+1] > listOfNumbers[i]:
#         count += 1
# print(f"Сумма чисел равна {count}")

result = sum([count+1 for i in range(len(listOfNumbers) - 1) if listOfNumbers[i+1] > listOfNumbers[i]])
print(f"Сумма чисел равна {result}")