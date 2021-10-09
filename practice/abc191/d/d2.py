def main():
    N = int(input())
    dp = [[0] * 2 for _ in range(N+1)]
    # dp[i][j]：xiまで決めたときのyiの場合の数
    dp[0][0] = dp[0][1] = 1
    for i in range(1, N+1):
        s = input()
        if s == 'AND':
            dp[i][0] = dp[i-1][0] * 2 + dp[i-1][1]
            dp[i][1] = dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1] * 2 + dp[i-1][0]

    return dp[-1][1]
