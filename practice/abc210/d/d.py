#!/usr/bin/env python3
def main():
    H, W, C=map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    INF = float("inf")
    ans = INF

    dp = [[INF]*W for _ in range(H)]
    dp[0][0] = A[0][0]
    dp[H-1][W-1] = A[H-1][W-1]
    for h in range(0, H):
        for w in range(0, W):
            if h != 0:
                dp[h][w] = min(dp[h][w], A[h][w], dp[h-1][w]+C)
                ans = min(ans, dp[h-1][w]+C+A[h][w])
            if w != 0:
                dp[h][w] = min(dp[h][w], A[h][w], dp[h][w-1]+C)
                ans = min(ans, dp[h][w-1]+C+A[h][w])


    dp=[[INF]*W for _ in range(H)]
    dp[0][-1] = A[0][-1]
    dp[0][W-1] = A[0][W-1]
    for h in range(0, H):
        for w in range(W-1, -1, -1):
            if h != 0:
                dp[h][w] = min(dp[h][w], A[h][w], dp[h-1][w]+C)
                ans = min(ans, dp[h-1][w]+C+A[h][w])
            if w != W-1:
                dp[h][w] = min(dp[h][w], A[h][w], dp[h][w+1]+C)
                ans = min(ans, dp[h][w+1]+C+A[h][w])
        
    return ans

print(main())

