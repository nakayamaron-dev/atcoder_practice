#!/usr/bin/env python3
def main():
    N, W = map(int,input().split())

    ws = [0]
    vs = [0]
    for i in range(N):
        w, v = list(map(int, input().split()))
        ws.append(w)
        vs.append(v)
    
    # dp[i][j]: 品物iまで見て重さ合計wであるときの価値の総和の最大値
    dp = [[-float("inf")]*(W+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        for j in range(W+1):

            # 品物iを使わない場合
            dp[i][j] = max(dp[i][j], dp[i-1][j])

            # 品物iを使う場合
            if j - ws[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-ws[i]] + vs[i])
    
    return max(dp[N])

print(main())

# not self AC
# ナップサック問題：二次元の状態を持つ動的計画法で解ける代表的な問題。