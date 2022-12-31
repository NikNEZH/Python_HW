# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.
# import random
# natural_number = random.randint(1, 10)
# sum =[]
# for i in range(1,11):
#     if natural_number % i == 0:
#         sum.append(i)
#         print(sum)

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    elif n == 1:
        Ans.append(n)
    return Ans

result = Factor(100)
print(result)