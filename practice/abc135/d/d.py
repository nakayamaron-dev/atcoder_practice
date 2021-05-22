#!/usr/bin/env python3
def main():
    S = input()
    mod = 10**9 + 7
    dp = [[0]*13 for _ in range(len(S)+1)]
    dp[0][0] = 1

    for i in range(len(S)):
        for j in range(13):
            for k in range(10):
                if S[i] == "?" or k == int(S[i]):
                    dp[i+1][(j*10+k) % 13] += dp[i][j]
                    dp[i+1][(j*10+k) % 13] %= mod
    
    return dp[-1][5]

print(main())

# not self AC
# 桁毎に分けてdpという難しい問題。
