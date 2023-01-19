# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = " а было бы возможно впереди быть ага"
print ("Исходная строка: " + str)
litter_a = "а"
litter_b = "б"
litter_v = "в"
result = ''
lol = lambda str,litter: str.replace(litter, '')
def fun (string, lamda,litter ):
    for i in range(0, len(string)):
        if litter in string[i]: return lamda(string,litter)
        continue
        return string
result = fun(str,lol,litter_a)
print(result)
result = fun(result,lol,litter_b)
print(result)
result = fun(result,lol,litter_v)
print(result)


