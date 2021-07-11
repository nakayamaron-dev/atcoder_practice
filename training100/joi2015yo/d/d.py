#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    D = [int(input()) for _ in range(N)]
    C = [int(input()) for _ in range(M)]

    # dp[i][j]: i日目に都市jにいる時の疲労度
    dp = [[0] + [float("INF")] * N for _ in range(M+1)]

    for i in range(M):
        for j in range(N):
            # i日目に移動した場合と、滞在した場合で疲労の少ない方をTakeする。
            dp[i+1][j+1] = min(dp[i][j] + D[j]*C[i], dp[i][j+1])
    
    return dp[-1][-1]

print(main())
