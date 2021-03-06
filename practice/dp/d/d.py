#!/usr/bin/env python3
N, W = map(int,input().split())
W_V = [list(map(int, input().split())) for l in range(N)]

# dp[i][j]: 最初のi個の品物までの中から重さがjを超えないように選んだときの、価値の最大値

def solve(N: int, W: int, W_V: [[int]]):
    dp = [[0] * (W+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(W+1):
            if j < W_V[i][0]: # i番目の品物を選べないとき

                # 価値は変わらない。
                dp[i+1][j] = dp[i][j]

            else: # i番目の品物を選べるとき

                # i番目の品物を選ぶ場合と選ばない場合で、価値の大きい方を採用する。
                dp[i+1][j] = max(dp[i][j], dp[i][j - W_V[i][0]] + W_V[i][1])
                
    return dp[-1][-1]

print(solve(N, W, W_V))

## not self AC