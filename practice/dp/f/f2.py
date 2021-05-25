#!/usr/bin/env python3
def main():
    S = input()
    T = input()
    n = len(S)
    m = len(T)

    # dp[i][j]: Sをi文字目、Tをj文字目までみたとき最長共通部分の長さ
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # sとtが同じ文字の場合、この文字を使うので、dp[i-1][j-1] + 1
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # sとtが違う文字の場合、どっちかの文字は使わないから、max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    ans = ""
    # dpを逆にたどっていく。
    while dp[n][m]:
        # 同じ文字の場合、答えに追加し、n, mからそれぞれ1を引く。
        if S[n-1] == T[m-1]:
            ans += S[n-1]
            n -= 1
            m -= 1
        elif dp[n][m] == dp[n-1][m]:
            n -= 1
        elif dp[n][m] == dp[n][m-1]:
            m -= 1
    
    return ans[::-1]

print(main())
        


