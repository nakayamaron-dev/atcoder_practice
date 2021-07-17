#!/usr/bin/env python3
def cmb(n, r, mod):
    x, y = 1, 1
    for i in range(r):
        x = x*(n-i) % mod
        y = y*(i+1) % mod
    
    # yで割ることと、pow(y, mod-2, mod)を掛けることは同義 (フェルマーの小定理)
    return x * pow(y, mod-2, mod) % mod

def main():
    W, H = map(int,input().split())
    MOD = 10**9 + 7
    W, H = W-1, H-1
    
    ans = cmb(W+H, min(W, H), MOD)

    return ans

print(main())