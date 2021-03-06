#!/usr/bin/env python3
N = int(input())
H = list(map(int, input().split()))

#dp[i]: 足場iにたどり着くまでに支払うコストの総和の最小値

def solve(N: int, H: [int]):
    dp = [float('inf')] * N
    dp[0] = 0
    for i in range(1, N):
        if i == 1:
            dp[i] = dp[0] + abs(H[1] - H[0])
        else:
            dp[i] = min(dp[i-1]+abs(H[i] - H[i-1]), dp[i-2]+abs(H[i] - H[i-2]))
    
    return dp[N-1]

print(solve(N, H))

## self AC

