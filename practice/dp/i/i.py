#!/usr/bin/env python3
n = int(input())
p = list(map(float, input().split()))

# dp[i][j]: i枚目のコインまで投げたとき、表が出たコインの数の方が多い確率(3000は上限枚数)
dp=[[0]*3000 for _ in range(3000)]
dp[0][0] = 1

for i in range(n):
    for j in range(i+1):
        # i+1枚目が表になる場合
        dp[i+1][j+1]+=dp[i][j]*p[i]
         # i+1枚目が裏になる場合
        dp[i+1][j]+=dp[i][j]*(1-p[i])

#表が過半数以上になる確率の総和を算出する。
ans = 0
for i in range(n//2+1, n+1):
    ans += dp[n][i]

print(ans)

## not self AC