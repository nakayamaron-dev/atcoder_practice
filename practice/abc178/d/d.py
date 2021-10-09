#!/usr/bin/env python3
S = int(input())
mod = 10**9 + 7

dp = [0]*(S+1)
dp[0] = 1

for s in range(1, S+1):
    for j in range(0, (s-3)+1):
        dp[s] += dp[j]
        dp[s] %= mod

print(dp[-1])
