#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    H = list(map(int, input().split()))
    dp = [0] * N
    
    for i in range(1, N):
        min_cost = 10**9 + 1
        if i < K:
            for j in range(1, i+1):
                cost = dp[i - j] + abs(H[i] - H[i-j])
                min_cost = min(min_cost, cost)
        else:
            for j in range(1, K+1):
                cost = dp[i - j] + abs(H[i] - H[i-j])
                min_cost = min(min_cost, cost)
        
        dp[i] = min_cost
    
    return dp[-1]

print(main())

# self AC
# pythonだとTLEになる。
