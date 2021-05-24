#!/usr/bin/env python3
def main():
    N, W = map(int,input().split())

    ws, vs = [], []
    for i in range(N):
        w, v = list(map(int, input().split()))
        ws.append(w)
        vs.append(v)
    
    # dp[i][j]: i番目までの品物を、価値がjになるように選んだときの最小の重さ。
    vmax = 10**5
    dp = [[float("inf")]*(vmax+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        for j in range(vmax+1):
            # 品物iを使う場合
            if j - vs[i-1] >= 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j - vs[i-1]] + ws[i-1])
            
            # 品物iを使わない場合
            dp[i][j] = min(dp[i][j], dp[i-1][j])
    
    for i, wmin in enumerate(dp[N]):
        if wmin <= W:
            ans = i
    
    return ans

print(main())

# not self AC
# pythonだとTLEになる。
