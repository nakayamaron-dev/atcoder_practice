#!/usr/bin/env python3
from collections import Counter
def main():
    N, M = map(int,input().split())
    A = [int(input()) for _ in range(M)]
    mod = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    cnt = Counter(A)

    for i in range(1, N+1):
        if cnt.get(i, 0) != 0: 
            continue

        if i == 1:
            dp[i] = 1
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % mod
    
    return dp[-1]

print(main())

# self AC
