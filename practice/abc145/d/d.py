#!/usr/bin/env python3
from math import modf


def main():
    X, Y = map(int,input().split())
    d = X + Y
    mod = 10**9 + 7
    
    if d % 3 != 0:
        return 0
    
    n = (2*Y - X) // 3
    m = (2*X - Y) // 3
    if n < 0 or m < 0:
        return 0

    a, b = 1, 1
    for i in range(min(n, m)):
        # n+mCnの分子、分母をそれぞれ算出する。 
        a = a*(n+m-i) % mod
        b = b*(i+1) % mod
    
    # フェルマーの小定理によりn+mCnを求める。
    ans = (a*pow(b, mod-2, mod)) % mod

    return ans

print(main())

# (i+1, j+2)の移動をA、(i+2, j+1)の移動をBとし、Aをa回、Bをｂ回行うとする。
# a + 2b = X
# 2a + b = Y
# の連立方程式を満たせば良い。
# つまり、X+Yが3の倍数でなければ移動は不可能。
# フェルマーの小定理を用いて、nCkを求める。

# not self AC
# フェルマーの小定理を勉強した。