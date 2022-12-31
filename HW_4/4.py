# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def creat_fail_two(tex):
    with open('file№2.txt', 'w') as data:
        data.write(tex)
def creat_fail(tex):
    with open('file№1.txt', 'w') as data:
        data.write(tex)

def rnd():
    return random.randint(0, 101)
def random_for_value(k):
    My_lst = [rnd() for i in range(k +1)]
    return My_lst

def create_str(sp):
    lst= sp[:]
    wr = ''
    for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += '+'
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += '+'
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]}=0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += '=0'
    return wr

k = int(input("Введите число для коэфициента первого файла"))

koef = random_for_value(k)
creat_fail(create_str(koef))

# Второй многочлен для следующей задачи:

k_two = int(input("Введите число для коэфициента второго файла"))
koef_for_file_two = random_for_value(k_two)
creat_fail_two(create_str(koef_for_file_two))
