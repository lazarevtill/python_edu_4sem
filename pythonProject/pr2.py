import math
from cmath import tan


def f11(x):
    ans = 27 * (x ** 5 + x ** 3) ** 2 + 57 * x ** 7 - (92 * x ** 7 - 66 * x ** 8) / (
            (x ** 4 / 42) - 4 * x ** 2 - 36) + tan(tan(x)) + 71 * x ** 6
    return ans


def f12(x):
    if x < -20:
        ans = 27 * (x ** 5 + x ** 3) ** 2 + 57 * x ** 7
    if -20 <= x < 67:
        ans = (x ** 3 / 33 + x ** 5 + 54) ** 8 - x ** 4 / 32
    if x >= 67:
        ans = 19 * (x ** 7 + 56 * x ** 5) + 19 * x ** 8
    return ans


def f13(n, m):
    ans1 = 0
    for i in range(1, n + 1):
        ans1 += (math.exp(1) ** i) + i - 36
    ans2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ans2 += (57 * (i ** 8)) - (84 * (i ** 3))
    ans = (71 * ans1) + (21 * ans2)
    return ans


def f14(n):
    ans = 0
    if n == 0:
        return 3
    if n == 1:
        return 5
    ans = math.sin(f14(n - 1)) - (1 / 8) * f14(n - 1) ** 2
    return ans

def f21(x):
    ans = 0
    if x[0] == '2018':
        if x[4] == "ragel":
            if x[1] == "rebol":
                if x[3] == 'sqf':
                    return 0
                if x[3] == 'awk':
                    return 1
                if x[3] == 'xbase':
                    return 2
            if x[1] == 'opa':
                return 3
        if x[4] == "click":
            return 4
        if x[4] == "io":
            if x[1] == 'rebol':
                return 5
            if x[1] == 'opa':
                return 6
    if x[0] == '2013':
        if x[4] == "ragel":
            return 7
        if x[4] == 'click':
            return 8
        if x[4] == 'io':
            if x[2] == "2018":
                if x[1] == 'rebol':
                    return 9
                if x[1] == 'opa':
                    return 10
            if x[2] == "2015":
                return 11


def f22(number):
    a = number & 0b00000000000000000000000000000001
    b = number & 0b00000000000000000000000000000010
    c = number & 0b00000000000000000000000011111100
    d = number & 0b00000000000000000000011100000000
    e = number & 0b00000000000000000011100000000000
    f = number & 0b00000001111111111100000000000000
    g = number & 0b11111110000000000000000000000000
    numb = (b << 30) | (d << 19) | (g >> 5) | (e << 5) | (c << 10) | (a << 11) | (f >> 14)
    return hex(numb)


def f23():


if __name__ == '__main__':
    # x = input().split()
    print()


