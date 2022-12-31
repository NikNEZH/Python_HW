# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
import re
from collections import defaultdict
from array import *

file1 = 'file№1.txt'
file2 = 'file№2.txt'
sum_file = 'sum_file'

# Получение данных из файла

def read_pol(file):
    with open(str(file), 'r') as data:
        polindrom = data.read()
    return polindrom
def write_to_pol(file, pol):
    with open(file, 'w') as data:
        data.write(pol)


# находим степени и коэфициенты
def search_values(txt):
    txt = txt.replace('=0', '')
    txt = txt.split('+')
    # txt = re.sub("[*|^| ]", " ", txt).split('+')
    # txt = [char.split(' ') for char in txt]
    # for i in txt:
    #     if i[0] == 'x': i.insert(0,1)
    return txt


pol_1 = read_pol(file1)
pol_2 = read_pol(file2)

print(pol_1)
print(pol_2)

c = search_values(pol_1)
a = search_values(pol_2)
j = c + a
print(j)
# # i = 1
# # while i < 7:
# if j[0][1] == j[4][1]:
#     c =int( " ".join(j[0][0].split('x')))
#     a =int( " ".join(j[4][0].split('x')))
#     b = c + a
#     print(f'{b}x^{j[0][1]} +')
#     print(j[1])
#     print(j[5])
#
# if j[1]:
#     z = int(" ".join(j[1].split('x')))
#     x = int(" ".join(j[5].split('x')))
#     g = c + a
#     print(f'{g}x^{j[1]} +')

mask = re.compile(r'(\d*)(x?\^?\d*)')

members_dict = defaultdict(list)
for member in j:
    result = mask.findall(member)
    if result:
        members_dict[result[0][1]].append(int(result[0][0] or 1))


to_save = '+'.join((f'{sum(value)}{key}' for key,value in members_dict.items()))
print(to_save)
write_to_pol(sum_file,to_save)


















