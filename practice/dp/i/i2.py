#!/usr/bin/env python3
def main():
    N = int(input())
    P = list(map(float, input().split()))

    # dp[i][j]: i枚目のコインまで投げたとき、表がj枚でる確率。
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    ans = 0

    for i in range(N):
        for j in range(i+1):
            #i+1枚目が表になる場合
            dp[i+1][j+1] += dp[i][j] * P[i]
            
            #i+1枚目が裏になる場合
            dp[i+1][j] += dp[i][j] * (1-P[i])
    
    for i in range(N//2+1, N+1):
        ans += dp[N][i]
    
    return ans

print(main())

# not self AC
