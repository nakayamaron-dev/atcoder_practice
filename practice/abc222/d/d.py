#!/usr/bin/env python3
def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    m = 3005
    mod = 998244353

    dp = [[0]*m for _ in range(n)]

    for j in range(A[0], B[0]+1):
        dp[0][j] += 1

    for i in range(n):
        for j in range(A[i], B[i]+1):
            if i > 0:
                dp[i][j] = dp[i-1][j]

        for j in range(m-1):
            dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= mod

    return dp[n-1][B[n-1]]


print(main())
