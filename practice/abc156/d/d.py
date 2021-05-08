#!/usr/bin/env python3
def cmb(n, r, mod):
    x, y = 1, 1
    for i in range(r):
        x = x*(n-i) % mod
        y = y*(i+1) % mod
    
    # yで割ることと、pow(y, mod-2, mod)を掛けることは同義 (フェルマーの小定理)
    return x * pow(y, mod-2, mod) % mod

def main():
    import math
    n, a, b = map(int,input().split())
    mod = 10**9 + 7

    ans = pow(2, n, mod) - 1
    ans -= cmb(n, min(a, n-a), mod)
    ans -= cmb(n, min(b, n-b), mod)

    return ans % mod

print(main())

# not self AC
# フェルマーの小定理
