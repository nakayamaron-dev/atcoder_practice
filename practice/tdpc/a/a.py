#!/usr/bin/env python3
def main():
    n = int(input())
    # 1はじまりにするために先頭にダミーを入れる。
    p = [0] + list(map(int, input().split()))
    P = sum(p)

    #dp[i][j]: iまでの問題で得点合計をjにできるかどうか / bool
    dp = [[False]*(P+1) for _ in range(n+1)]
    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(P+1):
            # 問題iを解かない場合
            if dp[i-1][j]:
                dp[i][j] = True
            
            # 問題iを解く場合
            if j >= p[i] and dp[i-1][j-p[i]]:
                dp[i][j] = True
    
    ans = 0
    for i in range(P+1):
        if dp[n][i]:
            ans += 1
        
    return ans

print(main())

