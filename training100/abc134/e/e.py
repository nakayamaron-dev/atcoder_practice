#!/usr/bin/env python3
from bisect import bisect_left,bisect_right
def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    dp = [-1] * N

    for i in range(N):
        dp[bisect_left(dp, A[i]) - 1] = A[i]
    
    return N - bisect_left(dp, 0)

print(main())