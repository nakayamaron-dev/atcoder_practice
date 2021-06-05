#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353

    dp = [0] * N
    dp[0] = 1
    sdp = [0] * (N+1)
    sdp[1] = 1

    for i in range(1, N):
        print(i)
        for l, r in LR:
            left = max(0, i - r)
            right = max(0, i - l + 1)
            dp[i] += sdp[right] - sdp[left]
            dp[i] %= mod
        
        sdp[i+1] = (sdp[i] + dp[i] % mod)
    
    return dp[-1]

print(main())


# 累積和＋DPの問題
# なんとなくは分かったが、自力では解けない。

