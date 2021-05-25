#!/usr/bin/env python3
def main():
    H, W = map(int,input().split())
    A = [input() for _ in range(H)]
    mod = 10**9+7

    # dp[i][j]: (i, j)にたどり着く場合の数
    dp = [[0]*(W) for _ in range(H)]
    dp[0][0] = 1

    for h in range(H):
        for w in range(W):
            # A[h][w]が空白マスの場合、右から来る場合と上から来る場合の場合の数を足す。
            if A[h][w] == ".":
                dp[h][w] += (dp[h-1][w] + dp[h][w-1]) % mod
    
    return dp[-1][-1]

print(main())