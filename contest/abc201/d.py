H, W = map(int,input().split())
A = [input() for _ in range(H)]

dp = [[0]*W for _ in range(H)]

for i in reversed(range(H)):
    for j in reversed(range(W)):
        if i == H-1 and j == W-1:
            continue
        
        dp[i][j] = - float("inf")

        if i+1 < H:
            score = 1 if A[i+1][j] == "+" else -1
            dp[i][j] = max(dp[i][j], -dp[i+1][j] + score)

        if j+1 < W:
            score = 1 if A[i][j+1] == '+' else -1
            dp[i][j] = max(dp[i][j], -dp[i][j+1] + score)

if dp[0][0] == 0: print("Draw")
if dp[0][0] > 0: print("Takahashi")
if dp[0][0] < 0: print("Aoki") 
