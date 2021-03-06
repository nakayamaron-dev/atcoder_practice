#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

#dp[l][r]: 間[l,r]が残ってるときの「次の手番の人の得点－そうじゃない方の人の得点」
dp=[[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for l in range(N-i+1):
        r = i + l

        # 先頭を選んだ場合の、自分の得点 - 相手の得点(最適)
        dpl = A[l] - dp[l+1][r]
        # 末尾を選んだ場合の、自分の得点 - 相手の得点(最適)
        dpr = A[r-1] - dp[l][r-1]

        dp[l][r] = max(dpl, dpr) # 先頭を選んだ場合と末尾を選んだ場合で値が大きい方を採用する。

print(dp[0][N])

## not self AC
