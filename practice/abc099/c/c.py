N = int(input())

# dp[i]: i円支払うのに必要な操作の最小回数
dp = [10**6]*(N+1)
dp[0] = 0

for i in range(1, N+1):
    j = 1
    while j <= i:
        dp[i] = min(dp[i-j]+1, dp[i])
        j *= 6
    k = 1
    while k <= i:
        dp[i] = min(dp[i-k]+1, dp[i])
        k *= 9

print(dp[N])

# not self AC
# 動的計画法の習熟度を向上する必要あり。