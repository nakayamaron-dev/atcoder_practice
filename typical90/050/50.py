#!/usr/bin/env python3
def main():
    N, L = map(int,input().split())
    MOD = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1

    for i in range(1, N+1):
        if i < L:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-L]
        
        dp[i] %= MOD
    
    return dp[N] % MOD

print(main())