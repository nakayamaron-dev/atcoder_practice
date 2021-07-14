#!/usr/bin/env python3
from bisect import bisect_left,bisect_right

def main():
    N = int(input())
    C = [int(input()) for _ in range(N)]

    dp = [float("inf")] * N

    for i in range(N):
        dp[bisect_left(dp, C[i])] = C[i]
    
    return N - bisect_left(dp, float("inf"))

print(main())