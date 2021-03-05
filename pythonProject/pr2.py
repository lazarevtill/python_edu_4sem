import math
from cmath import tan


#
#
# def f11(x):
#     ans = 27 * (x ** 5 + x ** 3) ** 2 + 57 * x ** 7 - (92 * x ** 7 - 66 * x ** 8) / (
#             (x ** 4 / 42) - 4 * x ** 2 - 36) + tan(tan(x)) + 71 * x ** 6
#     return ans
#
#
# def f12(x):
#     if x < -20:
#         ans = 27 * (x ** 5 + x ** 3) ** 2 + 57 * x ** 7
#     if -20 <= x < 67:
#         ans = (x ** 3 / 33 + x ** 5 + 54) ** 8 - x ** 4 / 32
#     if x >= 67:
#         ans = 19 * (x ** 7 + 56 * x ** 5) + 19 * x ** 8
#     return ans
#
#
# def f13(n, m):
#     ans1 = 0
#     for i in range(1, n + 1):
#         ans1 += (math.exp(1) ** i) + i - 36
#     ans2 = 0
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             ans2 += (57 * (i ** 8)) - (84 * (i ** 3))
#     ans = (71 * ans1) + (21 * ans2)
#     return ans
#
#
# def f14(n):
#     ans = 0
#     if n == 0:
#         return 3
#     if n == 1:
#         return 5
#     ans = math.sin(f14(n - 1)) - (1 / 8) * f14(n - 1) ** 2
#     return ans
#
#
def f21(x):
    if x[0] == 2018:
        if x[4] == 'io':
            if x[1] == "opa":
                return 6
            else:
                return 5
        elif x[4] == 'click':
            return 4
        else:
            if x[1] == 'rebol':
                if x[3]=="xbase":
                    return 2
                elif x[3]=="awk":
                    return 1
                else:
                    return 0
            else:
                return 3
    elif x[0] == 2013:
        if x[4] == 'ragel':
            return 7
        elif x[4] == 'io':
            if x[2] == 2018:
                if x[1]=="rebol":
                    return 9
                else:
                    return 10
            else:
                return 11
        else:
            return 8


def f22(number):
    a = number & 0b00000000000000000000000000000001
    print("a",bin(a))
    b = number & 0b00000000000000000000000000000010
    print("b",bin(b))
    c = number & 0b00000000000000000000000001111100
    print("c",bin(c))
    d = number & 0b00000000000000000000001110000000
    print("d",bin(d))
    e = number & 0b00000000000000000001110000000000
    print("e",bin(e))
    f = number & 0b00000000111111111110000000000000
    print("f",bin(f))
    g = number & 0b11111110000000000000000000000000
    print("g",bin(g))
    numb = (b << 30) | (d << 19) | (g >> 5) | (e << 5) | (c << 10) | (a << 11) | (f >> 14)
    return bicn(numb)
#
#
# def f23():
#
#
# if __name__ == '__main__':
#     # x = input().split()
#     print()
x = 0x14ac443a




def f22(number):
    a = number & 0b00000000000000000000000000000001
    b = number & 0b00000000000000000000000000000010
    c = number & 0b00000000000000000000000011111100
    d = number & 0b00000000000000000000011100000000
    e = number & 0b00000000000000000011100000000000
    f = number & 0b00000001111111111100000000000000
    g = number & 0b11111110000000000000000000000000
    numb = (b << 30) | (d << 19) | (g >> 5) | (e << 5) | (c << 10) | (a << 11) | (f >> 14)
    return numb

print(f22_1(x))
print(x)