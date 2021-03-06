#!/usr/bin/env python3
N = int(input())
A_B_C = [list(map(int, input().split())) for l in range(N)]

def solve(N: int, A_B_C: [[int]]):
    dp = [[0] * 3 for i in range(N+1)]

    for i in range(1, N+1):
        dp[i][0] = A_B_C[i-1][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = A_B_C[i-1][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = A_B_C[i-1][2] + max(dp[i-1][1], dp[i-1][0])

    return max(dp[-1])

print(solve(N, A_B_C))

## not self AC