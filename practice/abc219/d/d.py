#!/usr/bin/env python3
def main():
    INF = float("inf")
    N = int(input())
    X, Y = map(int, input().split())
    dp = [[[INF] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = 0

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(X+1):
            nj = min(j+a, X)
            for k in range(Y+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                nk = min(k+b, Y)
                dp[i+1][nj][nk] = min(dp[i+1][nj][nk], dp[i][j][k]+1)

    return dp[N][X][Y] if dp[N][X][Y] < INF else -1


print(main())
