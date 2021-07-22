#!/usr/bin/env python3
def main():
    K = int(input())
    MOD = 10**9 + 7

    # 桁和が9の倍数でなければ9の倍数にならない。
    if K % 9 != 0:
        return 0

    dp = [1] * (K+1)
    for i in range(1, K):
        if i-9 >= 0:
            dp[i+1] = (dp[i]*2 - dp[i-9]) % MOD
        else:
            dp[i+1] = (dp[i]*2) % MOD
    
    return dp[K]

print(main())

# |oo|ooo|o|ooo|
# k個のoの分割の仕方をdpで数える。
# 丸の個数が各位の数にあたる(上の例だと2313)
# 最初と最後に必ず|を置き、oは10個以上連続させない。
# dp[i]...i個のoの分割数
# dp[i+1] = dp[i] + dp[i-1] + ... + dp[i-8]
#         = dp[i] + dp[i-1] + ... + dp[i-8] + dp[i-9] - dp[i-9]
#         = dp[i] + dp[i] - dp[i-9]
#         = dp[i]*2 - dp[i-9]