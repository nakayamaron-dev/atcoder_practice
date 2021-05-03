#!/usr/bin/env python3
from collections import deque
def main():
    n, x, y = map(int,input().split())
    k = 201
    x += k
    y += k

    # 始点からの最小移動回数を管理する2次元配列。-1であれば未訪問
    dist = []
    for i in range(404):
        dist.append([-1]*404)
    
    # 障害物のマスには-2を格納
    for _ in range(n):
        a, b = map(int,input().split())
        dist[a+k][b+k] = -2
    
    # キューを用意して始点を格納
    q = deque()
    q.append([k, k])
    dist[k][k] = 0

    while len(q) > 0:
        i, j = q.popleft()

        for i2, j2 in [[i+1, j+1],[i, j+1],[i-1, j+1],[i+1, j],[i-1, j],[i, j-1]]:
            #もし盤面の範囲内でなければ無視
            if not (0 <= i2 < 404 and 0 <= j2 < 404):
                continue
            # もし未訪問であれば、距離を更新していキューに入れる
            if dist[i2][j2] == -1:
                dist[i2][j2] = dist[i][j] + 1
                q.append([i2, j2])
    
    return dist[x][y]

print(main())

# not self AC
