#!/usr/bin/env python3
def main():
    N, W = map(int,input().split())

    ws = [0]
    vs = [0]
    for i in range(N):
        w, v = list(map(int, input().split()))
        ws.append(w)
        vs.append(v)

    # dp[i][j]: 品物iまで見て重さ合計jであるときの価値の総和の最大値
    dp = [[-float("inf")]*(W+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        for j in range(W+1):
            # 品物iを使わない場合
            dp[i][j] = max(dp[i-1][j], dp[i][j])

            # 品物iを使う場合
            if j >= ws[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-ws[i]] + vs[i])
    
    return max(dp[-1])

print(main())

# not self AC
