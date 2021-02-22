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


if __name__ == '__main__':
    x = input().split()
    print(f21(x))
f(0x14ac443a) = 0xa0a0e2b1

