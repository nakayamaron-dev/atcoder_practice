#!/usr/bin/env python3
def main():
    n, m = map(int,input().split())
    a = [int(input()) for _ in range(m)]

    dp = [0] * (n+1)
    dp[0] = 1
    mod = 10**9 + 7

    if 1 not in a:
        dp[1] = 1

    for i in range(2,n+1):
        if i not in a:
            dp[i] = (dp[i-1] + dp[i-2]) % mod
    
    return dp[-1]

print(main())
        
# not self AC            
            