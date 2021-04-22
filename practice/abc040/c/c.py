#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [0]*N
    dp[1] = abs(A[0] - A[1])
    
    for i in range(2, N):
        dp[i] = min(dp[i-1]+abs(A[i-1]-A[i]), dp[i-2]+abs(A[i-2]-A[i]))
    
    return dp[-1]

print(main())

# self AC
