# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
tchn = int(input('введите заданную точность'))
def calc_pi(eps=1e-4):
    s = 0
    d = 1
    sgn = 1
    while True:
        a = 4 / d
        s = s + sgn * a
        if a < eps:
            return s
        sgn = -sgn
        d += 2


print(round(calc_pi(),tchn))