#!/usr/bin/env python3
def main():
    N = int(input())
    H = list(map(int, input().split()))

    dp = [0] * N
    dp[1] = abs(H[1] - H[0])

    for i in range(2, N):
        ptn1 = dp[i-1] + abs(H[i] - H[i-1])
        ptn2 = dp[i-2] + abs(H[i] - H[i-2])
        dp[i] = min(ptn1, ptn2)
    
    return dp[-1]

print(main())

# self AC
