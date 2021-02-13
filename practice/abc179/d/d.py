#!/usr/bin/env python3
N, K = map(int,input().split())
LR = [list(map(int, input().split())) for l in range(K)]

mod = 998244353
dp = [0]*N
dp[0] = 1
sdp = [0]*(N+1)
sdp[1] = 1

for i in range(N):
    for lr in LR:
        dp[i] += sdp[max(i-lr[0]+1, 0)] - sdp[max(i-lr[1], 0)]
    dp[i] %= mod
    sdp[i+1] = sdp[i]+dp[i]

print(dp[N-1])

# 区間の和は累積和を使う。dpの問題
