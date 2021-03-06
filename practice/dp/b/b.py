#!/usr/bin/env python3
N, K = map(int,input().split())
H = list(map(int, input().split()))

def solve(N: int, K: int, H: [int]):
    dp = [float('inf')] * N
    dp[0] = 0

    for i in range(1, N):
        if i == 1:
            dp[i] = dp[0] + abs(H[1]-H[0])
        else:
            dp[i] = min([dp[i-itm] + abs(H[i] - H[i-itm]) for itm in range(1, K+1)])
    
    return dp[N-1]

print(solve(N, K, H))

## self AC