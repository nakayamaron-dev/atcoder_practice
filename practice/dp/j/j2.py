#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # dp[c1][c2][c3]: 1個の皿がc1枚、2個の皿がc2枚、3個の皿がc3枚あるとき、全て食べるまでの操作回数の期待値
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

    def rec(i, j, k):
        if dp[i][j][k] != 0 or i==j==k==0:
            return dp[i][j][k]
        
        tmp = 1
        if i > 0:
            tmp += rec(i-1, j, k) * i/N
        if j > 0:
            tmp += rec(i+1, j-1, k) * j/N # 2つ残っている皿から一つ食べると1つ残っている皿が1枚増えることに注意。
        if k > 0:
            tmp += rec(i, j+1, k-1) * k/N
        
        dp[i][j][k] = tmp / (1-(N-i-j-k)/N)

        return dp[i][j][k]
    
    x, y, z = [A.count(i) for i in [1, 2, 3]]

    return rec(x, y, z)

print(main())

# (1-(N-i-j-k)/N)：(1-(0個の皿が選ばれる確率))
# かなり難しい問題