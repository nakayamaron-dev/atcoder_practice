#!/usr/bin/env python3
# DFS
# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

h, w = map(int,input().split())
s = [input() for _ in range(h)]

# 始点と終点の座標を探し、それぞれ(si,sj)と(gi,gj)とする。
for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            si, sj = i, j

        if s[i][j] == "g":
            gi, gj = i, j

# 訪問済みかどうかを管理する配列
visited = []
for i in range(h):
        visited.append([False] * w)

# 再帰関数dfsを実装
def dfs(i, j):
    visited[i][j] = True

    for i2, j2 in [[i+1, j],[i-1, j],[i, j+1],[i, j-1]]:
        if not (0 <= i2 < h and 0 <= j2 < w):
            continue
        if s[i][j] == "#":
            continue
        if not visited[i2][j2]:
            dfs(i2, j2)

# 始点から呼び出す。
dfs(si, sj)

if visited[gi][gj]:
    print("Yes")
else:
    print("No")

# not self AC    
# main関数にすると、MLEになる。
# pypyで実行すると、TLE, MLEになる。(pypyは再帰処理が弱い。)
