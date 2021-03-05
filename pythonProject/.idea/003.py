from math import tan
def f11(x):
    return 27 * (x ** 5 + x ** 3) ** 2 + 57 * x ** 7 - (92 * x ** 7 - 66 * x ** 8) / (
                x ** 4 / 42 - 4 * x ** 2 - 36) + tan(tan(x)) + 71 * x ** 6

print(f11(24))