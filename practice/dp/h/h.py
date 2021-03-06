#!/usr/bin/env python3
h, w = map(int,input().split())
a = [input() for _ in range(h)]

# dp[i][j]: (i, j)にたどり着く場合の数

dp = [[0]*(w) for _ in range(h)]
dp[0][0] = 1
mod = 10**9+7

for i in range(h):
    for j in range(w):
        # a[i][j]が'.'の時、左から、上から移動してくるdpを更新する。
        if a[i][j] == '.':
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % mod

print(dp[-1][-1])


