#!/usr/bin/env python3
def main():
    N = int(input())
    S = list(input())
    MOD = 10007

    X = []
    for s in S:
        if s == "J":
            X.append(1)
        elif s == "O":
            X.append(2)
        else:
            X.append(4)
    
    # dp[i][bs]: i日目にbsという人の組み合わせを使う時の通り数
    # 0日目を作って初期値にJ君がいる状態を作る。
    dp = [[0] * 8 for _ in range(N+1)]
    dp[0][1] = 1

    for i, x in enumerate(X, start=1):
        for bs in range(1, 8):
            if not (x & bs):
                continue

            for pre_bs in range(1, 8):
                if bs & pre_bs:
                    dp[i][bs] += dp[i-1][pre_bs]
                    dp[i][bs] %= MOD
    
    return sum(dp[-1]) % MOD

print(main())