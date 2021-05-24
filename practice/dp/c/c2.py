#!/usr/bin/env python3
def main():
    N = int(input())
    ABC = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*3 for _ in range(N+1)]

    for i in range(1, N+1):
        # i-1日目にAを選んだ場合のi日目の幸福度の最大
        dp[i][0] = ABC[i-1][0] + max(dp[i-1][1], dp[i-1][2])

        # i-1日目にBを選んだ場合
        dp[i][1] = ABC[i-1][1] + max(dp[i-1][0], dp[i-1][2])

        # i-1日目にCを選んだ場合
        dp[i][2] = ABC[i-1][2] + max(dp[i-1][0], dp[i-1][1])
    
    return max(dp[-1])

print(main())

# not self AC
