#!/usr/bin/env python3
# dp[i][j][k]: x1~xiからj枚選んでxiの合計をkにするような選び方の総数
def main():
    N, A = map(int,input().split())
    X = list(map(int, input().split()))

    dp = [[[0 for i in range(N*A+1)] for j in range(N+1)] for k in range(N+1)]
    dp[0][0][0] = 1

    for i in range(1, N+1):
        for j in range(N+1):
            for k in range(N*A+1):
                if k - X[i-1] < 0:
                    dp[i][j][k] = dp[i-1][j][k]
                else:
                    dp[i][j][k] = dp[i-1][j-1][k-X[i-1]] + dp[i-1][j][k]

    ans = 0
    for i in range(1, N+1):
        ans += dp[N][i][i*A]
    
    return ans

print(main())

# not self AC
# 難しい。
