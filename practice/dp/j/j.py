#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

# A[i]: i枚目の皿にのっている寿司の数。
# dp[c1][c2][c3]: 1個の皿がc1枚、2個の皿がc2枚、3個の皿がc3枚あるとき、全て食べるまでの操作回数の期待値
dp=[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

def f(i: int, j: int, k: int,):
    # 一度算出済み or 全ての寿司がなくなった場合
    if dp[i][j][k] != 0 or i==j==k==0:
        return dp[i][j][k]
    
    tmp = 1
    if i > 0: tmp += f(i-1, j, k) * i/N
    if j > 0: tmp += f(i+1, j-1, k) * j/N
    if k > 0: tmp += f(i, j+1, k-1) * k/N
    
    dp[i][j][k] = tmp / (1-(N-i-j-k)/N)

    return dp[i][j][k]

x, y, z = [A.count(i) for i in [1,2,3]]

print(f(x, y, z))

# not self AC

# 考え方
# dp[c1][c2][c3]=
# 1+
# dp[c1−1][c2][c3]∗(1個の皿が選ばれる確率)+
# dp[c1+1][c2−1][c3]∗(2個の皿が選ばれる確率)+
# dp[c1][c2+1][c3−1]∗(3個の皿が選ばれる確率)+
# dp[c1][c2][c3]∗(0個の皿が選ばれる確率)
# ↓
# dp[c1][c2][c3]=
# 1/(1−(0個の皿が選ばれる確率))+
# dp[c1−1][c2][c3]∗(1個の皿が選ばれる確率)/(1−(0個の皿が選ばれる確率))+
# dp[c1+1][c2−1][c3]∗(2個の皿が選ばれる確率)/(1−(0個の皿が選ばれる確率))+
# dp[c1][c2+1][c3−1]∗(3個の皿が選ばれる確率)/(1−(0個の皿が選ばれる確率))

