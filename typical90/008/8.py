#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()
    MOD = 10**9 + 7
    #r,er,der,oder,coder,tcoder,atcoder
    l = [0]*7

    for i in range(1, N+1):
        t = S[-i]
        if t == "r":
            l[0] += 1
        elif t == "e":
            l[1] += l[0]
        elif t == "d":
            l[2] += l[1]
        elif t == "o":
            l[3] += l[2]
        elif t == "c":
            l[4] += l[3]
        elif t == "t":
            l[5] += l[4]
        elif t == "a":
            l[6] += l[5]

    return l[-1] % MOD

print(main())

# 耳DPというやつらしい。
