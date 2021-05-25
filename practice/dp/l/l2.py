#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))

    # dp[l][r]: [l, r]が残っているときの「次の手番人の得点 - そうじゃない方の人の得点」の最適値
    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for l in range(N+1 - i):
            r = l + i

            # 先頭を選んだ場合の得点差
            dpl = A[l] - dp[l+1][r]

            # 末尾を選んだ場合の得点差
            dpr = A[r-1] - dp[l][r-1]

            # 先頭と末尾で、より得点差が大きくなる方を選ぶ。
            dp[l][r] = max(dpl, dpr)
    
    return dp[0][N]

print(main())

# not self AC
    