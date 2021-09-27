#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # 前の状態で次の状態が決まるので、DP
    dp = [[0]*10 for _ in range(N)]
    dp[1][(A[0]*A[1]) % 10] += 1
    dp[1][(A[0]+A[1]) % 10] += 1

    for i in range(2, N):
        y = A[i]

        for x in range(10):
            dp[i][(x*y) % 10] += dp[i-1][x]
            dp[i][(x*y) % 10] %= MOD

            dp[i][(x+y) % 10] += dp[i-1][x]
            dp[i][(x+y) % 10] = dp[i][(x+y) % 10] % MOD

    for i in range(10):
        print(dp[N-1][i])


main()
