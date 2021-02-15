import math


def oneone(x):
    ans = 27 * (x ** 5 + x ** 3) ** 2 + 57 * x ** 7 - (92 * x ** 7 - 66 * x ** 8) / (
            (x ** 4 / 42) - 4 * x ** 2 - 36) + math.tan(math.tan(x)) + 71 * x ** 6
    print(ans)


def onetwo(x):
    if x < -20:
        ans = 27 * (x ** 5 + x ** 3) ** 2 + 57 * x ** 7
    if -20 <= x < 67:
        ans = (x ** 3 / 33 + x ** 5 + 54) ** 8 - x ** 4 / 32
    if x >= 67:
        ans = 19 * (x ** 7 + 56 * x ** 5) + 19 * x ** 8
    print(ans)


def onethree(n, m):
    ans1 = 0
    for i in range(1, n):
        ans1 += (math.e ** i) + i - 36
    ans2 = 0
    for i in range(1, n):
        for j in range(1, m):
            ans2 += (57 * (i ** 8)) - (84 * (i ** 3))
    ans = (71 * ans1) + (21 * ans2)
    print(ans)


def onefour(n):
    ans = 0
    if n==0:
        return 3
    if n==1:
        return 5
    ans = math.sin(onefour(n - 1)) - (1 / 8) * onefour(n - 1) ** 2
    return ans


if __name__ == '__main__':
    x = int(input())
    # oneone(x)
    # onetwo(x)

    # y = int(input())
    # onethree(x, y)

    print(onefour(x))
