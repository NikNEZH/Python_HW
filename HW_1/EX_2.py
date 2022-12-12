# Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def getNumbers (x):
    a = []
    for i in range(x):
        a.append(input("Введите число: "))
    return a


def check(x):
    approveOne = not (x[0] or x[1] or x[2])
    approveTwo = not x[0] and not x[1] and not x[2]
    result = approveOne == approveTwo
    return result


newArgument = getNumbers(3)

if check(newArgument) == True:
    print("Выражение верно")
else:
    print("Выражение не верно")



