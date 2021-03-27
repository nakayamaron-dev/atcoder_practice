#!/usr/bin/env python3
N, M = map(int,input().split())
A = set([int(input()) for _ in range(M)])

# dp[i]: i段目までの上り方の総数 
dp = [0]*(N+1)
dp[0] = 1
mod = 1000000007

if not (1 in A):
    dp[1] = 1

for i in range(2, N+1):
    if not (i in A):
        dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[-1])

# not self AC
