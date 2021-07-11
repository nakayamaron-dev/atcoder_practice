#!/usr/bin/env python3
def main():
    N = int(input())
    S = [input() for _ in range(5)]
    
    # dp[i][j]: i列目を色jに塗る時の塗り替えのmin
    dp = [[float("INF")]*3 for _ in range(N+1)]
    dp[0] = [0, 0, 0]

    #各列の色毎の数を管理する配列
    cnt = [[0]*3 for _ in range(N)]

    for i in range(5):
        for j in range(N):
            if S[i][j] == "R":
                cnt[j][0] += 1
            elif S[i][j] == "B":
                cnt[j][1] += 1
            elif S[i][j] == "W":
                cnt[j][2] += 1
    
    for i in range(N):
        # kをjに色変する
        for j in range(3):
            for k in range(3):
                if k == j: continue

                dp[i+1][j] = min(dp[i+1][j], dp[i][k]+(5-cnt[i][j]))
    
    return min(dp[N])

print(main())