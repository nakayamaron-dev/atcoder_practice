#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)

M = int(input())
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

ans = 0

def dfs(i, j, d):
    global ans
    visited[i][j] = True

    # 上下左右それぞれ探索
    for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:

        # マスの外側には行けない
        if not (0 <= x < N and 0 <= y < M):
            continue

        # 遷移先に薄氷がない場合
        if S[x][y] == 0:
            continue

        # 薄氷かつ未訪問の場合、cntをインクリメントし、再帰dfs
        if visited[x][y] == False:
            dfs(x, y, d+1)
    
        ans = max(ans, d)

#スタート地点を全探索
for i in range(N):
    for j in range(M):
        visited = [[False]*M for _ in range(N)]

        if S[i][j] == 1:
            dfs(i, j, 1)

print(ans)

# start地点は薄氷のあるマス全探索する必要がある。
# 上下左右に薄氷がある場合進むことができる。
# 最大何個薄氷を割ることができるか。
# 再帰でDFSで求めていく。

# 上記でWAになる理由がわからない。
