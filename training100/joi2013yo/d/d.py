#!/usr/bin/env python3
def main():
    D, N = map(int,input().split())
    T = [int(input()) for _ in range(D)]
    ABC = [list(map(int, input().split())) for _ in range(N)]
    a, b, c = [list(i) for i in zip(*ABC)]

    # dp: i日目服jを選んだ場合の派手さの差の絶対値の合計
    dp = [[0]*N for _ in range(D)]

    # 日付
    for i in range(1, D):
        tmp_j = 0

        # 同日選ぶ服
        for j in range(N):
            if a[j] <= T[i] <= b[j]:
                # 前日選んだ服
                for k in range(N):
                    if a[k] <= T[i-1] <= b[k]:
                        dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(c[k]-c[j]))
    
    return max(dp[-1])

print(main())
