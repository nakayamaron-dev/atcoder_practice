#!/usr/bin/env python3
import math
def main():
    N = int(input())
    T = list(map(int, input().split()))
    S = sum(T)

    # Tの部分集合を用いてS/2より大きい数値かつ最小のものを作る。
    # dp[i]: Tの部分集合を用いて合計iを作れるか。
    dp = [False] * (S+1)
    dp[0] = True

    for t in T:
        for i in range(S, t-1, -1):
            # tを見ている場合、i-tが作れるならばiも作れる。
            dp[i] |= dp[i-t]
    
    ans = math.ceil(S/2)

    # Tの総和の半分から一つずつインクリメントしていき、作れる数がでてきたらそれが答えになる。
    while dp[ans] == False:
        ans += 1
    
    return ans

print(main())