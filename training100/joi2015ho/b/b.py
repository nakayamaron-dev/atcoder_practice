#!/usr/bin/env python3
def main():
    N = int(input())
    C = [int(input()) for _ in range(N)]
    ans = 0

    # dp[i][j]: 残り[i, j]の状況から始めたときのJOIくんの取り分の最大値
    dp = [[0]*N for _ in range(N)]

    for i in range(1, N+1):
        for l in range(N):
            r = (l+i-1) % N
            
            # JOIくんのターン
            if (N-i) % 2 == 0:
                dp[l][r] = max(dp[l][(r-1)%N] + C[r], dp[(l+1)%N][r] + C[l])
            # IOIくんのターン
            else:
                if C[l] < C[r]:
                    dp[l][r] = dp[l][(r-1)%N]
                else:
                    dp[l][r] = dp[(l+1)%N][r]
    
    for i in range(N):
        ans = max(ans, dp[i][(i+N-1)%N])
    
    return ans

print(main())
                