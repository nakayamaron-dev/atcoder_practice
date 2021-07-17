#!/usr/bin/env python3
def cmb(n, r, mod):
    x, y = 1, 1
    for i in range(r):
        x = x*(n-i) % mod
        y = y*(i+1) % mod
    
    # yで割ることと、pow(y, mod-2, mod)を掛けることは同義 (フェルマーの小定理)
    return x * pow(y, mod-2, mod) % mod

def main():
    N = int(input())
    K = int(input())
    MOD = 10**9 + 7

    return cmb(N-1+K, N-1, MOD)

print(main())

# 重複あり組み合わせ
# nHk = n-1+k C n-1の公式がある。