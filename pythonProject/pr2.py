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


def f23()

if __name__ == '__main__':
    # x = input().split()
    print()


