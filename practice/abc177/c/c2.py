#!/usr/bin/env python3

# 方針
# 2重ループではTLEになりそう。
# 累積和を使って解く

N = int(input())
A = list(map(int, input().split()))

accum = 0
Sum = sum(A)
ans = 0
mod = 10**9 + 7
for i in range(N):
    accum += A[i]
    ans += A[i]*(Sum - accum)

print(ans % mod)

# self AC
