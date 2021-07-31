#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()
    MOD = 10**9 + 7
    dp = [0] * 7

    for s in S[::-1]:
        if s == "r":
            dp[0] += 1
        elif s == "e":
            dp[1] += dp[0]
        elif s == "d":
            dp[2] += dp[1]
        elif s == "o":
            dp[3] += dp[2]
        elif s == "c":
            dp[4] += dp[3]
        elif s == "t":
            dp[5] += dp[4]
        elif s == "a":
            dp[6] += dp[5]
        else:
            continue
    
    return dp[-1] % MOD

print(main())