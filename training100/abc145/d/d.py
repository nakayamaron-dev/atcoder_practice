#!/usr/bin/env python3
def cmb(n, r, mod):
    x, y = 1, 1
    for i in range(r):
        x = x*(n-i) % mod
        y = y*(i+1) % mod
    
    # yで割ることと、pow(y, mod-2, mod)を掛けることは同義 (フェルマーの小定理)
    return x * pow(y, mod-2, mod) % mod

def main():
    X, Y = map(int,input().split())
    MOD = 10**9 + 7

    if (X+Y) % 3 != 0 or max(X,Y)/min(X,Y) > 2:
        return 0
    
    n = (X+Y) // 3
    r = min(X, Y) - n

    ans = cmb(n, r, MOD)
    return ans

print(main())