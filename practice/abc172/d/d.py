#!/usr/bin/env python3
N = int(input())

def g(n: int):
    return n*(n+1) / 2

ans = 0
for k in range(1, N+1):
    ans += k * g(N//k)

print(int(ans))

 # not self AC
 # 愚直にやるとTLEになる。
 # 各倍数の和を足していく方式