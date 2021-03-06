#!/usr/bin/env python3
s = input()
t = input()
n = len(s)
m = len(t)

# dp[i][j]: sをi文字目、tをj文字目までみた時の最長共通部分列の長さ
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ""
while dp[n][m]:
    if s[n-1] == t[m-1]:
        n -= 1
        m -= 1
        ans += s[n]
    elif dp[n][m] == dp[n-1][m]:
        n -= 1
    elif dp[n][m] == dp[n][m-1]:
        m -= 1

print(ans[::-1])

# not self AC
# PypyじゃないとTLEになる。