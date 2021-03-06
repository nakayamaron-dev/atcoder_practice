#!/usr/bin/env python3
N, M = map(int,input().split())
lst_edge = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())

    # 最初のindexをゼロにするために全て1を引いてlistに格納
    lst_edge[x-1].append(y-1)

    # dp[v] := ノードvを始点とした時の有向パスの長さの最大値
    # -1 未訪問で初期化。
    dp = [-1] * N

    # メモ化再帰
    def rec(v):
        # 既に更新済み
        if dp[v] != -1:
            return dp[v]
        
        ans = 0
        for nv in lst_edge[v]:
            ans = max(ans, rec(nv)+1)
        dp[v] = ans

        return dp[v]

    ans = 0
    for v in range(N):
        ans = max(ans, rec(v))
    
print(ans)



