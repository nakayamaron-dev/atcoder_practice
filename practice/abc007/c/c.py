#!/usr/bin/env python3
# BFS
from collections import deque
def main():
    r, c = map(int,input().split())
    sy, sx = map(int,input().split())
    gy, gx = map(int,input().split())

    s = []
    for _ in range(r):
        tmp = input()
        s.append(tmp)
    
    #座標調整
    sx -= 1
    sy -= 1
    gx -= 1
    gy -= 1

    # 始点からの最小移動回数を管理する2次元配列。-1であれば未訪問
    dist = []
    for i in range(r):
        dist.append([-1]*c)
    
    # キューを用意して始点を入れる
    q = deque()
    q.append([sy, sx])
    dist[sy][sx] = 0

    # キューを取り出しながら探索
    while len(q) > 0:
        i, j = q.popleft()

        # 4つの隣のマスを確認
        for i2, j2 in [[i+1, j],[i-1, j],[i, j+1],[i, j-1]]:
            #もし盤面の範囲内でなければ無視
            if not (0 <= i2 < r and 0 <= j2 < c):
                continue
            # 壁マスであれば無視
            if s[i][j] == "#":
                continue
            # もし未訪問であれば、距離を更新していキューに入れる
            if dist[i2][j2] == -1:
                dist[i2][j2] = dist[i][j] + 1
                q.append([i2, j2])
        
    return dist[gy][gx]

print(main())

# not self AC
# 二次元グリッドを動く問題を、グラフの問題として考えて幅優先探索で解く。
# 最小移動回数を求める問題は幅優先探索で解ける。
