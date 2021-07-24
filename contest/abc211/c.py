def main():
    S = input()
    MOD = 10**9 + 7

    dp = [0] * 8
    #chokudai

    for i in range(1, len(S) + 1):
        t = S[-i]

        if t == "i":
            dp[0] += 1
        elif t == "a":
            dp[1] += dp[0]
        elif t == "d":
            dp[2] += dp[1]
        elif t == "u":
            dp[3] += dp[2]
        elif t == "k":
            dp[4] += dp[3]
        elif t == "o":
            dp[5] += dp[4]
        elif t == "h":
            dp[6] += dp[5]
        elif t == "c":
            dp[7] += dp[6]
    
    return dp[-1] % MOD

print(main())