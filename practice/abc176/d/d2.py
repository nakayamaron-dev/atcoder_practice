#!/usr/bin/env python3
from collections import deque


def main():
    H, W = map(int, input().split())
    CH, CW = map(int, input().split())
    DH, DW = map(int, input().split())
    S = [input() for _ in range(H)]
    INF = 10**9

    # 座標がずれているのでデクリメント
    CH -= 1
    CW -= 1
    DH -= 1
    DW -= 1

    q = deque()
    cost = [[INF]*W for _ in range(H)]

    # 初期化
    q.append((CH, CW))
    cost[CH][CW] = 0

    while q:
        h, w = q.popleft()
        for i in [-2, -1, 0, 1, 2]:
            for j in [-2, -1, 0, 1, 2]:
                # 次の候補地の座標を nh, nw とする。
                nh, nw = h + i, w + j
                dist = abs(i) + abs(j)

                # フィールドから出る or 壁の場合はスキップ
                if nh < 0 or H <= nh or nw < 0 or W <= nw or S[nh][nw] == "#":
                    continue

                # 隣接している場合はcost = 0で移動可能
                # 左にpush
                if dist <= 1:
                    cost[nh][nw] = min(cost[nh][nw], cost[h][w])
                    q.appendleft((nh, nw))

                # 離れている場合はcost = 1で移動可能
                # 右にpush
                else:
                    cost[nh][nw] = min(cost[nh][nw], cost[h][w] + 1)
                    q.append((nh, nw))

    return cost[DH][DW] if cost[DH][DW] < INF else -1


print(main())

# 01-BFS
# +0で遷移するものをappendで、+1で遷移するものをappendleftでdequeに追加
