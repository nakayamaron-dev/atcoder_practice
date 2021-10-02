def main():
    N, M = map(int, input().split())
    INF = 10 ** 18
    dp = [[INF] * N for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        dp[a - 1][b - 1] = c

    for i in range(N):
        dp[i][i] = 0

    ans = 0
    for k in range(N):
        for s in range(N):
            for t in range(N):
                dp[s][t] = min(dp[s][t], dp[s][k] + dp[k][t])
                if dp[s][t] < INF:
                    ans += dp[s][t]

    return ans


print(main())
