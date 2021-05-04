#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    A = [input() for _ in range(N)]

    # start(0) ~ goal(10)までの配列
    g = [[] for _ in range(11)]

    for i in range(N):
        for j in range(M):
            if A[i][j] == "S":
                n = 0
            elif A[i][j] == "G":
                n = 10
            else:
                n = int(A[i][j])
            
            g[n].append([i, j])
            
    #dp[i][j]:正しい順序でマス(i, j)に辿り着く最小移動回数
    dp = [[float("inf")] * M for _ in range(N)]
    si, sj = g[0][0]
    dp[si][sj] = 0

    for n in range(1, 11):
        for i, j in g[n]:
            for i2, j2 in g[n-1]:
                # abs(i-i2) + abs(j-j2) : マンハッタン距離
                dp[i][j] = min(dp[i][j], dp[i2][j2] + abs(i-i2) + abs(j-j2))
    
    gi, gj = g[10][0]
    ans = dp[gi][gj]

    if ans == float("inf"):
        return -1
    else:
        return ans

print(main())

# not self AC
# 経路をいくつかの工程い分ける、という考え方が重要。
# いくつかの工程に分けることで、一つ一つの工程が扱いやすくなり、工程がその切り替わる地点ごとに最小移動回数を求めていく動的計画法が適用できる。
